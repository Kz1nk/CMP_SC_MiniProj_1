# EEG Emotion Recognition Project - Research Answers

## Question 1: EEG Basics, Electrode Positioning, and Montages

### What is EEG (Electroencephalography)?

**Definition:** EEG is a non-invasive method to record the spontaneous electrical activity of the brain by placing electrodes on the scalp.

**How it Works:**
- Brain cells (neurons) communicate through electrical signals
- When millions of neurons fire simultaneously, they create electrical fields
- These electrical fields can be detected on the scalp surface
- EEG measures postsynaptic potentials of pyramidal neurons in the cortex
- The signals are amplified and recorded as waveforms on a computer screen or paper

**What EEG Measures - Brain Waves:**
EEG measures different frequency bands of brain activity:
- **Delta waves (0.5-4 Hz)**: Associated with deep sleep
- **Theta waves (4-8 Hz)**: Linked to light sleep, drowsiness, creativity, and memory
- **Alpha waves (8-13 Hz)**: Present during wakeful relaxation (eyes closed, meditation)
- **Beta waves (13-30 Hz)**: Associated with active thinking, focus, and alertness
- **Gamma waves (30-80 Hz)**: Related to cognitive processing

---

### Electrode Positioning Systems

**The 10-20 System:**
The International 10-20 system is the standard method for placing EEG electrodes on the scalp. Created by Herbert Jasper in 1957, it ensures consistent and reproducible electrode placement across different subjects and studies.

**How the 10-20 System Works:**
1. Uses anatomical landmarks:
   - **Nasion**: The bridge of the nose (between the eyes)
   - **Inion**: The bump at the back of the skull
   - **Preauricular points**: Points just in front of each ear

2. Divides the head into sections based on percentages:
   - Distances between electrodes are either 10% or 20% of the total skull length
   - Ensures proportional spacing regardless of head size

**Electrode Naming Convention:**
- **Letters** indicate brain region:
  - Fp = Frontopolar
  - F = Frontal
  - C = Central
  - T = Temporal
  - P = Parietal
  - O = Occipital
  
- **Numbers** indicate hemisphere and position:
  - Odd numbers (1, 3, 5, 7) = Left hemisphere
  - Even numbers (2, 4, 6, 8) = Right hemisphere
  - "z" = Midline (e.g., Cz, Fz)

**Example:** 
- Fp1 = Left frontopolar region
- C4 = Right central region
- Oz = Occipital midline

**Advanced Systems:**
- **10-10 System**: Uses 10% intervals throughout, providing higher resolution with more electrodes
- **10-5 System**: Even finer resolution with 5% intervals

---

### What is a Montage?

**Definition:** A montage is the specific arrangement and combination of electrode pairs used to display EEG signals. It determines which electrodes are compared to which, creating different "views" of brain activity.

**Why Montages Matter:**
- Different montages highlight different aspects of brain activity
- They help localize abnormal electrical activity
- Multiple montages should be used to confirm findings

---

### Types of Montages

#### 1. Bipolar Montages

**How They Work:**
- Compare adjacent electrodes to each other in chains
- Each channel shows the voltage difference between two neighboring scalp electrodes
- Both electrodes are over active brain areas

**Common Bipolar Montages:**
- **Longitudinal Bipolar (Double Banana)**: Chains run front-to-back (anterior-posterior)
- **Transverse Bipolar**: Chains run left-to-right across the head
- **Circumferential (Halo)**: Chains circle around the head

**How to Read Bipolar:**
- Look for "phase reversals" - points where waveforms flip direction
- Phase reversals indicate the location of maximum electrical activity

**Example:**
In a chain like Fp1-F3-C3-P3-O1, if you see the waveforms pointing up before C3 and down after C3, there's a phase reversal at C3, indicating that's where the signal is strongest.

#### 2. Referential Montages (Also Called Monopolar)

**How They Work:**
- Compare each scalp electrode to a single common reference point
- The reference is usually placed at a relatively "quiet" location
- All electrodes are compared to the same reference

**Common References:**
- **Ear/Mastoid Reference (A1, A2, or M1, M2)**: Behind the ears - relatively electrically quiet
- **Average Reference**: The average voltage of all electrodes
- **Vertex Reference (Cz)**: Midline central electrode
- **Linked Ears**: Both ears connected together

**How to Read Referential:**
- Upward deflection = electrode is more negative than reference
- Downward deflection = electrode is more positive than reference
- The electrode with the largest deflection shows maximum activity

---

### Differences Between Bipolar and Referential Montages

| Aspect | Bipolar Montage | Referential Montage |
|--------|----------------|---------------------|
| **Comparison** | Adjacent electrodes to each other | Each electrode to common reference |
| **Localization** | Uses phase reversals in chains | Direct - largest signal shows location |
| **Best For** | Detecting focal abnormalities | Seeing widespread patterns |
| **Noise Cancellation** | Better (nearby electrodes cancel common noise) | Less effective if reference is contaminated |
| **Signal Amplitude** | Can be misleading - shows differences | More directly shows actual voltage |
| **Complexity** | More complex to interpret | Simpler to interpret |
| **Risk** | Can cancel out diffuse activity | Reference can be contaminated with signal |

**Key Differences:**
1. **Bipolar** is like comparing neighboring houses' temperatures to each other
2. **Referential** is like comparing each house's temperature to a fixed thermometer outside town

**In Practice:**
- **Bipolar montages** are excellent for screening and finding focal abnormalities because phase reversals stand out clearly
- **Referential montages** are useful for clarifying which specific electrode has the maximum activity when bipolar results are ambiguous
- EEG interpretation should use BOTH types to get complete information

---

### Advantages of EEG Recordings

1. **Excellent Temporal Resolution**
   - Captures brain activity in real-time (millisecond precision)
   - Can detect rapid changes in brain states

2. **Non-Invasive and Safe**
   - No radiation exposure (unlike PET scans)
   - No instruments inserted into the brain
   - Virtually no risk to participants

3. **Low Cost**
   - Much cheaper than fMRI or PET scanning
   - Equipment is relatively affordable
   - Cost per participant: $1-3 for ERP studies vs $800 for fMRI

4. **Portable**
   - Modern EEG systems are wearable
   - Can record in natural environments
   - Ambulatory EEG allows recording during daily activities

5. **Easy to Use**
   - Quick setup compared to other neuroimaging
   - No special facilities required (unlike MRI)
   - Can be used at bedside

6. **Direct Measurement**
   - Measures electrical activity of neurons directly
   - Not an indirect measure like blood flow (fMRI/PET)

7. **Accessible**
   - Widely available in clinical and research settings
   - No special screening required (unlike MRI - no metal restrictions)

---

### Disadvantages of EEG Recordings

1. **Poor Spatial Resolution**
   - Cannot precisely localize deep brain structures
   - Skull diffuses and spreads electrical signals
   - Can only detect activity from large areas (≥6 cm²)
   - Depth limitation: signals from deep brain areas are weak

2. **Inverse Problem**
   - Multiple different brain activity patterns could produce the same scalp recording
   - Cannot definitively determine the source of signals
   - Mathematical solutions require assumptions

3. **Susceptible to Artifacts**
   - Eye blinks and movements contaminate signals
   - Muscle activity (EMG) creates noise
   - Electrical interference from environment
   - Movement artifacts from cables or electrodes

4. **Limited to Surface Activity**
   - Best detects activity from cortical surface
   - Poor at detecting subcortical structures (hippocampus, thalamus, etc.)
   - Cannot "see" inside sulci (folds in the brain)

5. **Requires Many Trials**
   - For Event-Related Potentials (ERPs), need 40+ trials per condition
   - Small signal-to-noise ratio requires averaging
   - Can be time-consuming

6. **Setup Requirements**
   - Electrode placement takes time and skill
   - Gel or paste needed for good conductivity
   - Hair preparation required (washing, no products)
   - Can be uncomfortable for participants

7. **Interpretation Complexity**
   - Requires expertise to read and interpret
   - Multiple montages needed for complete picture
   - Phase reversals and patterns require training

8. **Reference Dependency (for referential montages)**
   - No truly "neutral" reference exists
   - Reference contamination can affect all channels
   - Choice of reference impacts results

---

## Question 2: Dataset Structure - GAMEEMO

### Dataset Overview

You are working with the **GAMEEMO dataset** (Database for Emotion Recognition System Based on EEG Signals and Various Computer Games).

**Dataset Characteristics:**
- **Total Participants**: 28 subjects (ages 20-27)
- **Recording Device**: Emotiv EPOC+ (14-channel wireless EEG headset)
- **Electrode Positions**: AF3, AF4, F3, F4, F7, F8, FC5, FC6, O1, O2, P7, P8, T7, T8 (10-20 system)
- **Sampling Rate**: 128 Hz (after downsampling from original)
- **Emotions Tested**: 4 emotions
  - Boring (Low Arousal - Negative Valence)
  - Calm (Low Arousal - Positive Valence)
  - Horror (High Arousal - Negative Valence)
  - Funny (High Arousal - Positive Valence)

---

### Recording Protocol

**How Data Was Collected:**
1. Each participant played 4 different computer games
2. Each game was designed to elicit one specific emotion
3. Games played for 5 minutes each
4. **Total recording time per participant: 20 minutes**
   - Boring game: 5 minutes
   - Calm game: 5 minutes
   - Horror game: 5 minutes
   - Funny game: 5 minutes

**Additional Information:**
- Participants rated each game using SAM (Self-Assessment Manikin) form
- Ratings were on arousal and valence scales
- Both raw and preprocessed data available
- Data formats: .csv and .mat files
- You will work with data from participant **S01** in the `data/` folder

---

### Why This Dataset is Unique

**Novel Approach:**
- Uses computer games as emotional stimuli (newer method)
- Combines audiovisual stimuli in interactive gaming context
- Tests portable EEG device effectiveness
- More ecologically valid than static images or sounds

**Research showed:**
- Games are effective at eliciting targeted emotions
- Portable EEG devices (like Emotiv EPOC+) can capture meaningful emotional data
- Interactive gaming provides better emotional engagement than passive stimuli

---

### Dataset Structure Details

**What You'll Find in the Data:**
- 14 channels of EEG data (one per electrode)
- Continuous recording for each 5-minute game session
- Emotion labels (boring, calm, horror, funny)
- Self-assessment ratings from participants
- Preprocessed versions with artifacts removed

**For Your Project:**
You'll be:
1. Loading data from participant S01
2. Processing 20 minutes of EEG data (4 games × 5 minutes)
3. Training a neural network to classify the 4 emotions
4. Testing the model's ability to predict emotions from brain signals

---

## Summary Table: Quick Reference

| Topic | Key Information |
|-------|----------------|
| **EEG** | Non-invasive recording of brain's electrical activity from scalp |
| **Brain Waves** | Delta (sleep), Theta (drowsy), Alpha (relaxed), Beta (active) |
| **10-20 System** | Standard electrode placement using 10% and 20% skull measurements |
| **Bipolar Montage** | Compares adjacent electrodes; shows phase reversals |
| **Referential Montage** | Compares each electrode to common reference |
| **EEG Advantages** | Excellent temporal resolution, safe, low cost, portable |
| **EEG Disadvantages** | Poor spatial resolution, artifacts, requires expertise |
| **GAMEEMO Dataset** | 28 participants, 4 emotions, 5 min per game |
| **Total Recording Time** | **20 minutes per participant** (4 games × 5 minutes) |
| **Your Data** | Participant S01 in `data/` folder |
| **Emotions** | Boring, Calm, Horror, Funny |
| **Channels** | 14 EEG electrodes (Emotiv EPOC+) |

---

*These answers provide the foundation for understanding your EEG emotion recognition project. Make sure to cite these concepts in your written report and demonstrate understanding of both the technology and the specific dataset you're working with.*
