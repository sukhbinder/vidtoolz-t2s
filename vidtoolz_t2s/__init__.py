import vidtoolz
import soundfile as sf
from pathlib import Path
from kokoro_onnx import Kokoro
from kokoro_onnx.tokenizer import Tokenizer
import sys


def _check():
    if not Path('kokoro-v1.0.onnx').exists() or not Path('voices-v1.0.bin').exists():
        print('Error: kokoro-v0_19.onnx and voices.json must be in the current directory.')
        print('Download with:')

        print('  wget https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/kokoro-v1.0.onnx')
        print('  wget https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/voices-v1.0.bin')
        sys.exit(1)
        
def get_voices():
    _check()
    kokoro = Kokoro('kokoro-v1.0.onnx', 'voices-v1.0.bin')
    voices = list(kokoro.get_voices())
    return voices
    
def text_to_speech(text, voice, lang, output_file):
    kokoro = Kokoro('kokoro-v1.0.onnx', 'voices-v1.0.bin')
    tokenizer = Tokenizer()
    phonemes = tokenizer.phonemize(text, lang=lang)
    print(f'Generating speech using voice "{voice}"...')
    samples, sample_rate = kokoro.create(phonemes, voice=voice, speed=1.0, lang=lang, is_phonemes=True)
    wav_file = output_file.replace('.mp3', '.wav')
    sf.write(wav_file, samples, sample_rate)

def create_parser(subparser):
    parser = subparser.add_parser("t2s", description="Text to speech using kokoro for mac os")
    parser.add_argument('text', help='Text to convert to speech (use quotes if multi-word)')
    parser.add_argument('-v', '--voice', choices=get_voices(), default="hm_beta", help=f'Voice to use ')
    parser.add_argument('-l', '--lang', default='en-us', help='Language code: en-gb, en-us, fr-fr, ja, ko, cmn')
    parser.add_argument('-o', '--output', default='output.wav', help='Output wav file name')
    return parser


class ViztoolzPlugin:
    """ Text to speech using kokoro for mac os """
    __name__ = "t2s"

    @vidtoolz.hookimpl
    def register_commands(self, subparser):
        self.parser = create_parser(subparser)
        self.parser.set_defaults(func=self.run)

    def run(self, args):
        # add actual call here
        text_to_speech(args.text, args.voice, args.lang, args.output)
    
    def hello(self, args):
        # this routine will be called when "vidtoolz "t2s is called."
        print("Hello! This is an example ``vidtoolz`` plugin.")

t2s_plugin = ViztoolzPlugin()
