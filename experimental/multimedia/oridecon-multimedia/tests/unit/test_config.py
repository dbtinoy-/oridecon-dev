from oridecon.config import BaseConfig
from oridecon.multimedia.beat.config import BeatAnalysisConfig
from oridecon.multimedia.config import MultimediaConfig
from oridecon.multimedia.image.config import ImageConfig
from oridecon.multimedia.interpolate.config import InterpolationConfig
from oridecon.multimedia.music.config import MusicConfig
from oridecon.multimedia.tts.config import TTSConfig
from oridecon.multimedia.upscale.config import UpscaleConfig
from oridecon.multimedia.video.config import VideoConfig


def test_multimedia_config_is_base_config() -> None:
    assert issubclass(MultimediaConfig, BaseConfig)
    assert MultimediaConfig.config_section == "multimedia"


def test_multimedia_config_from_dict_nested() -> None:
    cfg = MultimediaConfig.from_dict({"music": {"backend": "ace-step"}})
    assert cfg.music.backend == "ace-step"


def test_default_config_has_all_seven_subsystem_configs() -> None:
    cfg = MultimediaConfig()
    assert isinstance(cfg.tts, TTSConfig)
    assert isinstance(cfg.music, MusicConfig)
    assert isinstance(cfg.video, VideoConfig)
    assert isinstance(cfg.image, ImageConfig)
    assert isinstance(cfg.upscale, UpscaleConfig)
    assert isinstance(cfg.interpolate, InterpolationConfig)
    assert isinstance(cfg.beat, BeatAnalysisConfig)
    assert cfg.storage_path_prefix == "multimedia/"
