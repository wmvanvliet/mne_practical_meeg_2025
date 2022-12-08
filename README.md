# Material for the MNE-Python workshop of Practical MEEG 2022

More info on the workshop: [http://practicalmeeg2022.org/](http://practicalmeeg2022.org/)

Authors of the material:

	- Britta Westner, Radboud University Nijmegen, Donders Institute
	- Alexandre Gramfort, Inria, CEA Neurospin
	- Denis A. Engemann, Inria, CEA Neurospin

## Before you arrive

Please make sure you do the following steps before the first hands-on session:

1. You will need to [download the data](https://doi.org/10.5281/zenodo.7405048).
2. You will need to [download the extra data](https://drive.google.com/file/d/1EE_pDY-i6zkS5qiysaGw6HiG9yRLL1y1/view?usp=share_link) that we will use in some tutorials.
3. You will need to have installed MNE-Python on your machine. See instructions at: https://mne.tools/stable/install/index.html
4. If you are not familiar with Python, we invite you to take the time to work on these tutorials:
[intro Python](intro_to_python/0a-Intro_Python.ipynb), [intro Numpy](intro_to_python/0b-Intro_Numpy.ipynb).

## Program

#### Day 1 (Wednesday December 14, 2022)

 - 08:30 – 09:00 Registration, with coffee/tea + Welcome & intro
 - 09:00 – 09:45 Lecture: Good scientific Practice (Maxime, Anne-Sophie, François)
 - 09:45 - 10:30 Lecture: Importing, cleaning, and preprocessing data (Johanna)
 - 10:30 – 12:30 Hands-on: [Preprocessing](1-Preprocessing.ipynb) using MNE-Python

 - 12:30 – 14:00 Lunch

 - 14.00 – 18:00 Toolbox Bouquet (online)

#### Day 2 (Thursday December 15, 2022)

 - 09:00 – 09:45 Panel discussion
 - 09:00 – 09:45 Lecture: Time-domain analysis (Robert)
 - 10:30 – 12:30 Hands-on: [Sensor-level analysis](2-Time_domain_evoked_responses.ipynb) using MNE-Python

 - 12:30 – 14:00 Lunch

 - 14:00 – 15:3 Lecture: Spectral / Time-frequency analysis (Natalie)
 - 15:30 – 17:30 Hands-on: [Time-frequency analysis](3-Time_frequency_analysis.ipynb) using MNE-Python
 - 17:30 – 18:00 Panel discussion

#### Day 3 (Friday December 16, 2022)

 - 09:00 – 10:30 Lecture: Source estimation (Britta)
 - 10:30 – 12:30 Hands-on: [Forward modelling](4-Forward_modelling.ipynb) and [Source estimation](5-Source_reconstruction.ipynb) using MNE-Python

 - 12:30 – 14:00 Lunch

 - 14:00 – 15:30 Lecture: Group-level analysis (Robert)
 - 15:30 – 17:30 Hands-on: [Group level analysis](6-Group_analysis.ipynb) using MNE-Python
 - 17:30 – 18:00 Panel discussion


### References and credit

The code from this tutorial is heavily inspired from this article:

	Mainak Jas, Eric Larson, Denis Engemann, Jaakko Leppakangas, Samu Taulu, Matti Hamalainen,
	and Alexandre Gramfort. 2018. A Reproducible MEG/EEG Group Study With the MNE Software:
	Recommendations, Quality Assessments, and Good Practices.
	Frontiers in Neuroscience. 12, doi: 10.3389/fnins.2018.00530

The MNE software when used in publications should be acknowledged using citations.

To cite MNE-C or the inverse imaging implementations provided by the MNE software, please use:

	A. Gramfort, M. Luessi, E. Larson, D. Engemann, D. Strohmeier, C. Brodbeck, L. Parkkonen,
	M. Hämäläinen, MNE software for processing MEG and EEG data, NeuroImage, Volume 86,
	1 February 2014, Pages 446-460, ISSN 1053-8119.

To cite the MNE-Python package, please use:

	A. Gramfort, M. Luessi, E. Larson, D. Engemann, D. Strohmeier, C. Brodbeck, R. Goj, M. Jas,
	T. Brooks, L. Parkkonen, M. Hämäläinen, MEG and EEG data analysis with MNE-Python,
	Frontiers in Neuroscience, Volume 7, 2013, ISSN 1662-453X.

