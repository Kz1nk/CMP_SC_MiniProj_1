#!/usr/bin/env python3
"""
EEG Emotion Recognition Training Script for FABRIC Server
Converted from Jupyter notebook for command-line execution
"""

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend for server
import matplotlib.pyplot as plt
import torch
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import os
import time
import argparse

# ============================================================================
# CONSTANTS
# ============================================================================

SAMPLE_RATE = 32  # (Hz)
GAMES = ["boring", "calm", "horror", "funny"]

# ============================================================================
# ARGUMENT PARSING
# ============================================================================

parser = argparse.ArgumentParser(description='Train EEG emotion recognition model')
parser.add_argument('--data_dir', type=str, default='data', 
                    help='Directory containing data files')
parser.add_argument('--electrode', type=str, default='T7',
                    help='Electrode to use (T7, T8, F3, F4, F7, F8, FC5, FC6)')
parser.add_argument('--clip_length', type=int, default=2,
                    help='Clip length in seconds')
parser.add_argument('--batch_size', type=int, default=32,
                    help='Batch size for training')
parser.add_argument('--n_epochs', type=int, default=100,
                    help='Number of training epochs')
parser.add_argument('--learning_rate', type=float, default=0.0001,
                    help='Learning rate for optimizer')
parser.add_argument('--output_dir', type=str, default='output',
                    help='Directory to save results')
args = parser.parse_args()

# Create output directory if it doesn't exist
os.makedirs(args.output_dir, exist_ok=True)

print("="*80)
print("EEG EMOTION RECOGNITION - FABRIC SERVER TRAINING")
print("="*80)
print(f"\nConfiguration:")
print(f"  Data directory: {args.data_dir}")
print(f"  Electrode: {args.electrode}")
print(f"  Clip length: {args.clip_length} seconds")
print(f"  Batch size: {args.batch_size}")
print(f"  Epochs: {args.n_epochs}")
print(f"  Learning rate: {args.learning_rate}")
print(f"  Output directory: {args.output_dir}")
print("="*80)

# ============================================================================
# START TIMING
# ============================================================================

total_start_time = time.time()

# ============================================================================
# DATA LOADING
# ============================================================================

print("\n[1/6] Loading data...")
data_load_start = time.time()

data = []
for game_id, game in enumerate(GAMES):
    filepath = os.path.join(args.data_dir, f"S01G{game_id + 1}AllChannels.csv")
    print(f"  Loading {filepath}...")
    game_data = pd.read_csv(filepath)
    game_data["game"] = game
    data.append(game_data)

data = pd.concat(data, axis=0, ignore_index=True)

data_load_time = time.time() - data_load_start
print(f"  Data loaded in {data_load_time:.2f} seconds")
print(f"  Total samples: {len(data)}")

# ============================================================================
# DATA VISUALIZATION
# ============================================================================

print("\n[2/6] Creating data visualization...")
viz_start = time.time()

fig, ax = plt.subplots(1, 1, figsize=(12, 6))
for game in GAMES:
    ax.plot(data[data["game"] == game][args.electrode], label=game)
ax.set_xlabel("Time (samples)")
ax.set_xticks(range(0, len(data), SAMPLE_RATE * 60 * 10))
ax.set_ylabel("mV")
ax.set_title(f"EEG Signal - Electrode {args.electrode}")
ax.legend()
ax.grid(True, alpha=0.3)

viz_filepath = os.path.join(args.output_dir, f'raw_signal_{args.electrode}.png')
plt.savefig(viz_filepath, dpi=150, bbox_inches='tight')
plt.close()

viz_time = time.time() - viz_start
print(f"  Visualization saved to {viz_filepath} ({viz_time:.2f} seconds)")

# ============================================================================
# PREPROCESSING
# ============================================================================

print("\n[3/6] Preprocessing data...")
preprocess_start = time.time()

# Select electrode and game columns
data = data[[args.electrode, "game"]]

# Split into clips
clipped_data = []
y = []
for game_id, game in enumerate(GAMES):
    game_samples = data[data['game'] == game][args.electrode].to_numpy()
    clips = np.array_split(
        game_samples, 
        len(game_samples) // (args.clip_length * SAMPLE_RATE)
    )
    clipped_data.extend(clips)
    y.extend([game_id] * len(clips))

# Remove edge effects
min_length = np.min([len(arr) for arr in clipped_data])
X = []
for array in clipped_data:
    X.append(array[:min_length])

X = np.vstack(X).astype(float)
y = np.array(y, dtype=int)

preprocess_time = time.time() - preprocess_start
print(f"  Preprocessing complete in {preprocess_time:.2f} seconds")
print(f"  X shape: {X.shape}")
print(f"  y shape: {y.shape}")
print(f"  Clips per emotion: {np.bincount(y)}")

# ============================================================================
# DATASET PREPARATION
# ============================================================================

print("\n[4/6] Preparing datasets...")
dataset_prep_start = time.time()

np.random.seed(123)

# Add an additional axis required by torch's Conv layers
X = np.expand_dims(X, 1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# Convert to torch tensors
X_train = torch.Tensor(X_train)
X_test = torch.Tensor(X_test)
y_train = torch.Tensor(y_train)
y_test = torch.Tensor(y_test)

print(f"  Train samples: {X_train.shape[0]}")
print(f"  Test samples: {X_test.shape[0]}")

# Dataset class
class LFPDataset(torch.utils.data.Dataset):
    def __init__(self, X, y):
        self.X = X
        self.y = y.long()

    def __len__(self):
        return len(self.X)

    def __getitem__(self, idx):
        return self.X[idx], self.y[idx]

# Batch generators
train_batch_generator = torch.utils.data.DataLoader(
    LFPDataset(X_train, y_train), 
    batch_size=args.batch_size,
    shuffle=True
)

test_batch_generator = torch.utils.data.DataLoader(
    LFPDataset(X_test, y_test), 
    batch_size=args.batch_size,
    shuffle=False
)

dataset_prep_time = time.time() - dataset_prep_start
print(f"  Dataset preparation complete in {dataset_prep_time:.2f} seconds")

# ============================================================================
# MODEL DEFINITION
# ============================================================================

print("\n[5/6] Building model...")

model = torch.nn.Sequential(
    torch.nn.Conv1d(1, 1, kernel_size=4, padding="same"),
    torch.nn.ReLU(),
    torch.nn.Conv1d(1, 1, kernel_size=4, padding="same"),
    torch.nn.Flatten(),
    torch.nn.Linear(64, 4),
    torch.nn.LogSoftmax(dim=1)
)

# Count parameters
total_params = sum(p.numel() for p in model.parameters())
trainable_params = sum(p.numel() for p in model.parameters() if p.requires_grad)

print(f"  Total parameters: {total_params:,}")
print(f"  Trainable parameters: {trainable_params:,}")

# ============================================================================
# TRAINING
# ============================================================================

print(f"\n[6/6] Training model for {args.n_epochs} epochs...")
training_start = time.time()

optimizer = torch.optim.Adam(model.parameters(), lr=args.learning_rate)

# Track metrics
history = {
    'train_loss': [],
    'train_acc': [],
    'test_loss': [],
    'test_acc': [],
    'epoch_times': []
}

for e in range(args.n_epochs):
    epoch_start = time.time()
    
    # Training phase
    model.train(True)
    train_loss = []
    train_acc = []
    
    for X_batch, y_batch in train_batch_generator:
        model.zero_grad()
        logits = model(X_batch).squeeze()
        loss = torch.nn.functional.nll_loss(logits, y_batch)
        loss.backward()
        optimizer.step()
        train_loss.append(loss.detach().numpy())
        
        prediction = torch.softmax(logits, dim=1).detach().numpy()
        prediction = np.argmax(prediction, axis=1)
        train_acc.append(accuracy_score(y_batch.detach().numpy(), prediction))

    # Validation phase
    model.train(False)
    test_loss = []
    test_acc = []
    
    with torch.no_grad():
        for X_batch, y_batch in test_batch_generator:
            logits = model(X_batch).squeeze()
            loss = torch.nn.functional.nll_loss(logits, y_batch)
            test_loss.append(loss.detach().numpy())

            prediction = torch.softmax(logits, dim=1).detach().numpy()
            prediction = np.argmax(prediction, axis=1)
            test_acc.append(accuracy_score(y_batch.detach().numpy(), prediction))

    # Record metrics
    epoch_time = time.time() - epoch_start
    avg_train_loss = np.mean(train_loss)
    avg_train_acc = np.mean(train_acc)
    avg_test_loss = np.mean(test_loss)
    avg_test_acc = np.mean(test_acc)
    
    history['train_loss'].append(avg_train_loss)
    history['train_acc'].append(avg_train_acc)
    history['test_loss'].append(avg_test_loss)
    history['test_acc'].append(avg_test_acc)
    history['epoch_times'].append(epoch_time)
    
    # Print progress every 10 epochs
    if (e + 1) % 10 == 0 or e == 0:
        print(f"  Epoch {e+1:3d}/{args.n_epochs}: "
              f"train_loss={avg_train_loss:.4f}, train_acc={avg_train_acc:.4f}, "
              f"test_loss={avg_test_loss:.4f}, test_acc={avg_test_acc:.4f} "
              f"({epoch_time:.2f}s)")

training_time = time.time() - training_start
total_time = time.time() - total_start_time

print(f"\nTraining complete in {training_time:.2f} seconds")
print(f"Average time per epoch: {np.mean(history['epoch_times']):.2f} seconds")

# ============================================================================
# SAVE MODEL
# ============================================================================

print("\nSaving model...")
model_path = os.path.join(args.output_dir, 'emotion_recognition_model.pth')
torch.save(model.state_dict(), model_path)
print(f"  Model saved to {model_path}")

# ============================================================================
# PLOT TRAINING HISTORY
# ============================================================================

print("\nCreating training history plots...")

fig, axes = plt.subplots(1, 2, figsize=(15, 5))

# Loss plot
axes[0].plot(history['train_loss'], label='Train Loss', linewidth=2)
axes[0].plot(history['test_loss'], label='Test Loss', linewidth=2)
axes[0].set_xlabel('Epoch')
axes[0].set_ylabel('Loss')
axes[0].set_title('Training and Test Loss')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Accuracy plot
axes[1].plot(history['train_acc'], label='Train Accuracy', linewidth=2)
axes[1].plot(history['test_acc'], label='Test Accuracy', linewidth=2)
axes[1].set_xlabel('Epoch')
axes[1].set_ylabel('Accuracy')
axes[1].set_title('Training and Test Accuracy')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
history_path = os.path.join(args.output_dir, 'training_history.png')
plt.savefig(history_path, dpi=150, bbox_inches='tight')
plt.close()
print(f"  Training history saved to {history_path}")

# ============================================================================
# TEST PREDICTIONS
# ============================================================================

print("\nMaking test predictions...")

# Test on first few samples
model.eval()
with torch.no_grad():
    sample_predictions = []
    sample_actuals = []
    
    for i in range(min(10, len(X_test))):
        a_clip = X_test[i:i+1]
        prediction = model(a_clip)
        prediction = torch.softmax(prediction, dim=1).detach().numpy()
        pred_class = int(np.argmax(prediction, axis=1)[0])
        actual_class = int(y_test[i])
        
        sample_predictions.append(pred_class)
        sample_actuals.append(actual_class)
        
        print(f"  Sample {i+1}: Predicted={GAMES[pred_class]}, "
              f"Actual={GAMES[actual_class]}, "
              f"Correct={'✓' if pred_class == actual_class else '✗'}")

# ============================================================================
# SAVE TIMING REPORT
# ============================================================================

print("\nGenerating timing report...")

report_path = os.path.join(args.output_dir, 'timing_report.txt')
with open(report_path, 'w') as f:
    f.write("="*80 + "\n")
    f.write("EEG EMOTION RECOGNITION - TRAINING TIME REPORT\n")
    f.write("="*80 + "\n\n")
    
    f.write("Configuration:\n")
    f.write(f"  Electrode: {args.electrode}\n")
    f.write(f"  Clip length: {args.clip_length} seconds\n")
    f.write(f"  Batch size: {args.batch_size}\n")
    f.write(f"  Epochs: {args.n_epochs}\n")
    f.write(f"  Learning rate: {args.learning_rate}\n\n")
    
    f.write("Timing Breakdown:\n")
    f.write(f"  Data loading:          {data_load_time:8.2f} seconds\n")
    f.write(f"  Visualization:         {viz_time:8.2f} seconds\n")
    f.write(f"  Preprocessing:         {preprocess_time:8.2f} seconds\n")
    f.write(f"  Dataset preparation:   {dataset_prep_time:8.2f} seconds\n")
    f.write(f"  Model training:        {training_time:8.2f} seconds\n")
    f.write(f"  {'':22s} {'-'*15}\n")
    f.write(f"  TOTAL TIME:            {total_time:8.2f} seconds ({total_time/60:.2f} minutes)\n\n")
    
    f.write("Training Statistics:\n")
    f.write(f"  Average epoch time:    {np.mean(history['epoch_times']):8.2f} seconds\n")
    f.write(f"  Final train accuracy:  {history['train_acc'][-1]:8.4f}\n")
    f.write(f"  Final test accuracy:   {history['test_acc'][-1]:8.4f}\n\n")
    
    f.write("Model Statistics:\n")
    f.write(f"  Total parameters:      {total_params:8,}\n")
    f.write(f"  Trainable parameters:  {trainable_params:8,}\n")
    f.write(f"  Training samples:      {X_train.shape[0]:8,}\n")
    f.write(f"  Test samples:          {X_test.shape[0]:8,}\n\n")
    
    f.write("="*80 + "\n")

print(f"  Timing report saved to {report_path}")

# ============================================================================
# FINAL SUMMARY
# ============================================================================

print("\n" + "="*80)
print("TRAINING COMPLETE!")
print("="*80)
print(f"\nTotal execution time: {total_time:.2f} seconds ({total_time/60:.2f} minutes)")
print(f"Training time only: {training_time:.2f} seconds ({training_time/60:.2f} minutes)")
print(f"Final test accuracy: {history['test_acc'][-1]:.4f}")
print(f"\nResults saved to: {args.output_dir}/")
print("  - emotion_recognition_model.pth (trained model)")
print("  - training_history.png (loss and accuracy plots)")
print(f"  - raw_signal_{args.electrode}.png (data visualization)")
print("  - timing_report.txt (detailed timing breakdown)")
print("="*80)
