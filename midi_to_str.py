import argparse
import os

import mido

import midi_util
from midi_util import VocabConfig, FilterConfig

if __name__ == "__main__":
    curr_dir = os.path.dirname(os.path.realpath(__file__))

    p = argparse.ArgumentParser()
    p.add_argument(
        "filename",
        type=str,
        help="The MIDI file to convert to text",
    )
    p.add_argument(
        "--output",
        type=str,
        required=False,
        help="Path to output text file",
    )
    p.add_argument(
        "--vocab_config",
        type=str,
        default=f"{curr_dir}/vocab_config.json",
        help="Path to vocab config file",
    )
    p.add_argument(
        "--filter_config",
        type=str,
        default=f"{curr_dir}/filter_config.json",
        help="Path to filter config file",
    )

    args = p.parse_args()

    cfg = VocabConfig.from_json(args.vocab_config)
    filter_cfg = FilterConfig.from_json(args.filter_config)

    mid = mido.MidiFile(args.filename)
    text = '\n'.join(midi_util.convert_midi_to_str(cfg, filter_cfg, mid))
    
    if args.output is not None:
        with open(args.output, "w") as f:
            f.write(text)
    else:
        print(text)
