# Prepare the group analysis from raw data

# this script needs the other datasets downloaded via datalad (or another
# download service for the open neuro dataset)

# imports
import os
import mne

# set up paths: data_path to where the raw data lies, extra_path for saving
data_path = os.path.expanduser(
    "~/Documents/teaching/practical_meeg_2022_data/ds000117")
extra_path = os.path.expanduser(
    "~/Documents/teaching/practical_meeg_2022_data/extra_data_mne")

# set up the dataset identifiers
datasets = ["sub-%02d" % ii for ii in range(11, 15)  if ii not in [5, 10]]

# set up path to raw data and for saving the evokeds list
raw_fname_templ = 'derivatives/meg_derivatives/%s/ses-meg/meg/%s_ses-meg_\
task-facerecognition_run-01_proc-sss_meg.fif'
evoked_fname_templ = 'group_analysis/%s_list-ave.fif'

for id in datasets:

    # adapt the path for the dataset
    raw_fname = os.path.join(data_path, (raw_fname_templ % (id, id)))

    raw = mne.io.read_raw_fif(raw_fname, preload=True)

    raw.set_channel_types({'EEG061': 'eog',  # actually EOG not EEG
                           'EEG062': 'eog',  # actually EOG not EEG
                           'EEG063': 'ecg'  # actually ECG not EEG
                         })

    # resample the data and filter
    raw.resample(300)
    raw.filter(0, 40)

    # get events before dropping channels
    events = mne.find_events(raw, stim_channel='STI101', verbose=True)

    # adapt events
    delay = int(round(0.0345 * raw.info['sfreq']))
    events[:, 0] = events[:, 0] + delay
    events = events[events[:, 2] < 20]  # take only events with code < 20

    # pick channels
    raw.pick_types(meg=True, ecg=True, eog=True)

    # event IDs
    event_id = {
    'face/famous/first': 5,
    'face/famous/immediate': 6,
    'face/famous/long': 7,
    'face/unfamiliar/first': 13,
    'face/unfamiliar/immediate': 14,
    'face/unfamiliar/long': 15,
    'scrambled/first': 17,
    'scrambled/immediate': 18,
    'scrambled/long': 19,
    }

    # cut epochs
    tmin = -0.5  # start of each epoch (500ms before the trigger)
    tmax = 1.0  # end of each epoch (1000ms after the trigger)
    baseline = (-0.2, 0)  # means from 200ms before to stim onset (t = 0)

    # compute SSP
    projs_eog, _ = mne.preprocessing.compute_proj_eog(
                        raw, n_mag=3, n_grad=3, average=True)
    projs_ecg, _ = mne.preprocessing.compute_proj_ecg(
                        raw, n_mag=3, n_grad=3, average=True)

    # create epochs
    picks = mne.pick_types(raw.info, meg=True, eog=False, ecg=False,
                           stim=False)
    reject = dict(grad=4000e-13, mag=4e-12)
    epochs = mne.Epochs(raw, events, event_id, tmin, tmax, proj=False,
                        baseline=baseline, picks=picks, reject=reject,
                        preload=True, reject_by_annotation=False)

    # and then we add the EOG and ECG projs
    epochs.add_proj(projs_eog[::3] + projs_ecg[::3])

    conditions = ['famous', 'unfamiliar', 'scrambled']
    evokeds_list = []
    for k, cond in enumerate(conditions):
        evokeds_list.append(epochs[cond].average().apply_proj().crop(-0.5, 1))
        evokeds_list[k].comment = cond  # update the name of the condition

    # check the data by plotting
    # mne.viz.plot_compare_evokeds(evokeds_list, picks='MEG2143')

    # save the data
    evoked_list_fname = os.path.join(extra_path, (evoked_fname_templ % id))
    mne.write_evokeds(evoked_list_fname, evokeds_list, overwrite=True)
