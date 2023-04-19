# Mozart Musical Dice

Playing around with Musikalisches Würfelspiele.

> "A [Musikalisches Würfelspiel](https://en.wikipedia.org/wiki/Musikalisches_W%C3%BCrfelspiel) (German for "musical dice game") was a system for using dice to randomly generate music from precomposed options. These games were quite popular throughout Western Europe in the 18th century. Several different games were devised, some that did not require dice, but merely choosing a random number."

"Musikalisches Würfelspiel," wikipedia.org. <https://en.wikipedia.org/wiki/Musikalisches_W%C3%BCrfelspiel> (accessed April 19, 2023).

This project was inspired by Stanford University's [Mozart Musical Dice Game](http://nifty.stanford.edu/2023/wayne-musical-dice-game/) nifty assignment.

## Directions

A *Musikalisches Würfelspiel* is a process for generating music by concatenating a random sequence of precomposed musical fragments. In this exercise, we will "compose" a Viennese waltz in the style of Mozart by playing a sequence of 32 WAV files that are chosen at random (from a set of 272) according to the results of throwing dice, as described below.

### Minuet

The minuet consists of a sequence of 16 musical phrases (numbered 0 to 15), each chosen at random. For the purposes of this project, a musical phrase is short musical fragment, approximately two seconds in length. To determine which WAV file to play for phrase *i*, roll *two fair dice*.

If the sum is *s*, then play `minueti-s.wav`. For example, if you roll an 8 for phrase 3, then play `minuet3-8.wav`. Note that each roll has 11 possible outcomes (2 through 12) but some outcomes (such as 7) are much more likely than others (such as 2 or 12).

### Trio

The trio consists of a sequence of 16 phrases (numbered 0 to 15), each chosen at random. To determine which WAV file to play for phrase *i*, roll *one fair die*.

If the result is *s*, then play `trioi-s.wav`. For example, if you roll a 6 for phrase 15, then play `trio15-6.wav`.

### Data files

The musical phrases have been provided as a set of WAV files. Each phrase was generated using the tools described in the [Credits](#credits) section below. The `piano` directory contains the 272 WAV files (11×16=176 for the minuet phrases and 6×16=96 for the trio phrases), using the naming conventions described above. Other directories (`clarinet`, `flute-harp`, and `mbira` contain the same 272 musical phrases, but generated using different musical instruments.

### Generating WAV Files

WAV files will be generated using randomly selected phrases as described above, creating and writing the new file

Unlike the original version of the assignment in which the new composition was created simply by playing the selected WAV files in turn, we will generate new WAV files using the [wave](https://docs.python.org/3/library/wave.html) module of the Python standard library and write them to disk to be played later.

### Playing WAV Files

To play the generated WAV files we will use the [simpleaudio](https://simpleaudio.readthedocs.io/en/latest/) package which "provides cross-platform, dependency-free audio playback capability for Python 3 on macOS, Windows, and Linux."

**Note:** when installing `simpleaudio` under WSL2 I encountered the following error:

```shell
fatal error: alsa/asoundlib.h: No such file or directory
```

This was resolved by installing `libasound2-dev` with

```shell
apt install libasound2-dev
```

## Credits

The 272 provided musical phrases were published in 1792 by Mozart's publisher Nikolaus Simrock and [attributed to Mozart](https://imslp.org/wiki/Musikalisches_W%C3%BCrfelspiel,_K.516f_(Mozart,_Wolfgang_Amadeus)). The WAV files were generated using [MuseScore](https://musescore.org/) and the open-source [MuseScore_General.sf3](https://musescore.org/en/handbook/3/soundfonts-and-sfz-files) soundfont; they were post-processed using [ffmpeg](https://ffmpeg.org/).
