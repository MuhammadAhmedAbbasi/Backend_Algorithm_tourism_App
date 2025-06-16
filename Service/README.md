# Phantom: Subject-Consistent Video Generation via Cross-Modal Alignment

<div align="center">
  
[![arXiv](https://img.shields.io/badge/arXiv%20paper-2502.11079-b31b1b.svg)](https://arxiv.org/abs/2502.11079)&nbsp;
[![project page](https://img.shields.io/badge/Project_page-More_visualizations-green)](https://phantom-video.github.io/Phantom/)&nbsp;
<a href="https://huggingface.co/bytedance-research/Phantom"><img src="https://img.shields.io/static/v1?label=%F0%9F%A4%97%20Hugging%20Face&message=Model&color=orange"></a>
</div>


> [**Phantom: Subject-Consistent Video Generation via Cross-Modal Alignment**](https://arxiv.org/abs/2502.11079)<br>
> [Lijie Liu](https://liulj13.github.io/)<sup> * </sup>, [Tianxiang Ma](https://tianxiangma.github.io/)<sup> * </sup>, [Bingchuan Li](https://scholar.google.com/citations?user=ac5Se6QAAAAJ)<sup> * &dagger;</sup>, [Zhuowei Chen](https://scholar.google.com/citations?user=ow1jGJkAAAAJ)<sup> * </sup>, [Jiawei Liu](https://scholar.google.com/citations?user=X21Fz-EAAAAJ), Gen Li, Siyu Zhou, [Qian He](https://scholar.google.com/citations?user=9rWWCgUAAAAJ), Xinglong Wu
> <br><sup> * </sup>Equal contribution,<sup> &dagger; </sup>Project lead
> <br>Intelligent Creation Team, ByteDance<br>

<p align="center">
<img src="assets/teaser.png" width=95%>
<p>

## 🔥 Latest News!
* May 27, 2025: 🎉 We have released the Phantom-Wan-14B model, a more powerful Subject-to-Video generation model.
* Apr 23, 2025: 😊 Thanks to [ComfyUI-WanVideoWrapper](https://github.com/kijai/ComfyUI-WanVideoWrapper/tree/dev) for adapting ComfyUI to Phantom-Wan-1.3B. Everyone is welcome to use it!
* Apr 21, 2025: 👋 Phantom-Wan is coming! We adapted the Phantom framework into the [Wan2.1](https://github.com/Wan-Video/Wan2.1) video generation model. The inference codes and checkpoint have been released.
* Apr 10, 2025: We have updated the [full version](https://arxiv.org/pdf/2502.11079v2) of the Phantom paper, which now includes more detailed descriptions of the model architecture and dataset pipeline.
* Feb 16, 2025: We proposed a novel subject-consistent video generation model, **Phantom**, and have released the [report](https://arxiv.org/pdf/2502.11079v1) publicly. For more video demos, please visit the [project page](https://phantom-video.github.io/Phantom/).


## 📑 Todo List
- [x] Inference codes and Checkpoint of Phantom-Wan-1.3B 
- [x] Checkpoint of Phantom-Wan-14B
- [ ] Checkpoint of Phantom-Wan-14B Pro
- [ ] Open source Phantom-Data
- [ ] Training codes of Phantom-Wan

## 📖 Overview
Phantom is a unified video generation framework for single and multi-subject references, built on existing text-to-video and image-to-video architectures. It achieves cross-modal alignment using text-image-video triplet data by redesigning the joint text-image injection model. Additionally, it emphasizes subject consistency in human generation while enhancing ID-preserving video generation.

## ⚡️ Quickstart

### Installation
Clone the repo:
```sh
git clone https://github.com/Phantom-video/Phantom.git
cd Phantom
```

Install dependencies:
```sh
# Ensure torch >= 2.4.0
pip install -r requirements.txt
```

### Model Download
| Models       | Download Link                                                                                                                                           |    Notes                      |
|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------|
| Phantom-Wan-1.3B      | 🤗 [Huggingface](https://huggingface.co/bytedance-research/Phantom/blob/main/Phantom-Wan-1.3B.pth)   | Supports both 480P and 720P
| Phantom-Wan-14B | 🤗 [Huggingface](https://huggingface.co/bytedance-research/Phantom/tree/main) | Supports both 480P and 720P

First you need to download the 1.3B original model of Wan2.1, since our Phantom-Wan model relies on the Wan2.1 VAE and Text Encoder model. Download Wan2.1-1.3B using huggingface-cli:
``` sh
pip install "huggingface_hub[cli]"
huggingface-cli download Wan-AI/Wan2.1-T2V-1.3B --local-dir ./Wan2.1-T2V-1.3B
```

Then download the Phantom-Wan-1.3B and Phantom-Wan-14B model:
``` sh
huggingface-cli download bytedance-research/Phantom --local-dir ./Phantom-Wan-Models
```
Alternatively, you can manually download the required models and place them in the `Phantom-Wan-Models` folder.

### Run Subject-to-Video Generation

#### Phantom-Wan-1.3B

- Single-GPU inference

``` sh
python generate.py --task s2v-1.3B --size 832*480 --ckpt_dir ./Wan2.1-T2V-1.3B --phantom_ckpt ./Phantom-Wan-Models/Phantom-Wan-1.3B.pth  --ref_image "examples/ref1.png,examples/ref2.png" --prompt "暖阳漫过草地，扎着双马尾、头戴绿色蝴蝶结、身穿浅绿色连衣裙的小女孩蹲在盛开的雏菊旁。她身旁一只棕白相间的狗狗吐着舌头，毛茸茸尾巴欢快摇晃。小女孩笑着举起黄红配色、带有蓝色按钮的玩具相机，将和狗狗的欢乐瞬间定格。" --base_seed 42
```

- Multi-GPU inference using FSDP + xDiT USP

``` sh
pip install "xfuser>=0.4.1"
torchrun --nproc_per_node=8 generate.py --task s2v-1.3B --size 832*480 --ckpt_dir ./Wan2.1-T2V-1.3B --phantom_ckpt ./Phantom-Wan-Models/Phantom-Wan-1.3B.pth  --ref_image "examples/ref3.png,examples/ref4.png" --dit_fsdp --t5_fsdp --ulysses_size 4 --ring_size 2 --prompt "夕阳下，一位有着小麦色肌肤、留着乌黑长发的女人穿上有着大朵立体花朵装饰、肩袖处带有飘逸纱带的红色纱裙，漫步在金色的海滩上，海风轻拂她的长发，画面唯美动人。" --base_seed 42
```

> 💡Note: 
> * Changing `--ref_image` can achieve single reference Subject-to-Video generation or multi-reference Subject-to-Video generation. The number of reference images should be within 4.
> * To achieve the best generation results, we recommend that you describe the visual content of the reference image as accurately as possible when writing `--prompt`. For example, "examples/ref1.png" can be described as "a toy camera in yellow and red with blue buttons".
> * When the generated video is unsatisfactory, the most straightforward solution is to try changing the `--base_seed` and modifying the description in the `--prompt`.

For more inference examples, please refer to "infer.sh". You will get the following generated results:

<table style="width: 100%; border-collapse: collapse; text-align: center; border: 1px solid #ccc;">
  <tr>
    <th style="text-align: center;">
      <strong>Reference Images</strong>
    </th>
    <th style="text-align: center;">
      <strong>Generated Videos (480P)</strong>
    </th>
  </tr>

  <tr>
    <td style="text-align: center; vertical-align: middle;">
      <img src="examples/ref1.png" alt="Image 1" style="height: 180px;">
      <img src="examples/ref2.png" alt="Image 2" style="height: 180px;">
    </td>
    <td style="text-align: center; vertical-align: middle;">
      <img src="examples/ref_results/result1.gif" alt="GIF 1" style="width: 400px;">
    </td>
  </tr>

  <tr>
    <td style="text-align: center; vertical-align: middle;">
      <img src="examples/ref3.png" alt="Image 3" style="height: 180px;">
      <img src="examples/ref4.png" alt="Image 4" style="height: 180px;">
    </td>
    <td style="text-align: center; vertical-align: middle;">
      <img src="examples/ref_results/result2.gif" alt="GIF 2" style="width: 400px;">
    </td>
  </tr>

  </tr>
  <tr>
    <td style="text-align: center; vertical-align: middle;">
      <img src="examples/ref5.png" alt="Image 5" style="height: 180px;">
      <img src="examples/ref6.png" alt="Image 6" style="height: 180px;">
      <img src="examples/ref7.png" alt="Image 7" style="height: 180px;">
    </td>
    <td style="text-align: center; vertical-align: middle;">
      <img src="examples/ref_results/result3.gif" alt="GIF 3" style="width: 400px;">
    </td>
  </tr>

  <tr>
    <td style="text-align: center; vertical-align: middle;">
      <img src="examples/ref8.png" alt="Image 8" style="height: 100px;">
      <img src="examples/ref9.png" alt="Image 9" style="height: 100px;">
      <img src="examples/ref10.png" alt="Image 10" style="height: 100px;">
      <img src="examples/ref11.png" alt="Image 11" style="height: 100px;">
    </td>
    <td style="text-align: center; vertical-align: middle;">
      <img src="examples/ref_results/result4.gif" alt="GIF 4" style="width: 400px;">
    </td>
  </tr>
</table>

#### Phantom-Wan-14B

- Single-GPU inference

``` sh
python generate.py --task s2v-14B --size 832*480 --frame_num 121 --sample_fps 24 --ckpt_dir ./Wan2.1-T2V-1.3B --phantom_ckpt ./Phantom-Wan-Models --ref_image "examples/ref12.png,examples/ref13.png" --prompt "扎着双丸子头，身着红黑配色并带有火焰纹饰服饰，颈戴金项圈、臂缠金护腕的哪吒，和有着一头淡蓝色头发，额间有蓝色印记，身着一袭白色长袍的敖丙，并肩坐在教室的座位上，他们专注地讨论着书本内容。背景为柔和的灯光和窗外微风拂过的树叶，营造出安静又充满活力的学习氛围。"
```

- Multi-GPU inference using FSDP + xDiT USP

``` sh
pip install "xfuser>=0.4.1"
torchrun --nproc_per_node=8 generate.py --task s2v-14B --size 832*480 --frame_num 121 --sample_fps 24 --ckpt_dir ./Wan2.1-T2V-1.3B --phantom_ckpt ./Phantom-Wan-Models  --ref_image "examples/ref14.png,examples/ref15.png,examples/ref16.png" --dit_fsdp --t5_fsdp --ulysses_size 8 --ring_size 1 --prompt "一位戴着黄色帽子、身穿黄色上衣配棕色背带的卡通老爷爷，在装饰有粉色和蓝色桌椅、悬挂着彩色吊灯且摆满彩色圆球装饰的清新卡通风格咖啡馆里，端起一只蓝色且冒着热气的咖啡杯，画面风格卡通、清新。"
```

> 💡Note: 
> * The currently released Phantom-Wan-14B model was trained on 480P data but can also be applied to generating videos at 720P and higher resolutions, though the results may be less stable. We plan to release a version further trained on 720P data in the future.
> * The Phantom-Wan-14B model was trained on 24fps data, but it can also generate 16fps videos, similar to the native Wan2.1. However, the quality may experience a slight decline.
> * It is recommended to generate horizontal videos, as they tend to produce more stable results compared to vertical videos.

For more inference examples, please refer to "infer.sh". You will get the following generated results:

<table style="width: 100%; border-collapse: collapse; text-align: center; border: 1px solid #ccc;">
  <tr>
    <th style="text-align: center;">
      <strong>Reference Images</strong>
    </th>
    <th style="text-align: center;">
      <strong>Generated Videos (720P)</strong>
    </th>
  </tr>

  <tr>
    <td style="text-align: center; vertical-align: middle;">
      <img src="examples/ref12.png" alt="Image 1" style="height: 180px;">
      <img src="examples/ref13.png" alt="Image 2" style="height: 180px;">
    </td>
    <td style="text-align: center; vertical-align: middle;">
      <img src="examples/ref_results/result5.gif" alt="GIF 1" style="width: 400px;">
    </td>
  </tr>

  <tr>
    <td style="text-align: center; vertical-align: middle;">
      <img src="examples/ref17.png" alt="Image 3" style="height: 150px;">
      <img src="examples/ref18.png" alt="Image 4" style="height: 150px;">
    </td>
    <td style="text-align: center; vertical-align: middle;">
      <img src="examples/ref_results/result7.gif" alt="GIF 2" style="width: 400px;">
    </td>
  </tr>

  </tr>
  <tr>
    <td style="text-align: center; vertical-align: middle;">
      <img src="examples/ref14.png" alt="Image 5" style="height: 120px;">
      <img src="examples/ref15.png" alt="Image 6" style="height: 120px;">
      <img src="examples/ref16.png" alt="Image 7" style="height: 120px;">
    </td>
    <td style="text-align: center; vertical-align: middle;">
      <img src="examples/ref_results/result6.gif" alt="GIF 3" style="width: 400px;">
    </td>
  </tr>

</table>

> The GIF videos are compressed.


## Acknowledgements
We would like to express our gratitude to the SEED team for their support. Special thanks to Lu Jiang, Haoyuan Guo, Zhibei Ma, and Sen Wang for their assistance with the model and data. In addition, we are also very grateful to Siying Chen, Qingyang Li, and Wei Han for their help with the evaluation.

## ⭐ Citation

If Phantom is helpful, please help to ⭐ the repo.

If you find this project useful for your research, please consider citing our [paper](https://arxiv.org/abs/2502.11079).

### BibTeX
```bibtex
@article{liu2025phantom,
  title={Phantom: Subject-consistent video generation via cross-modal alignment},
  author={Liu, Lijie and Ma, Tianxiang and Li, Bingchuan and Chen, Zhuowei and Liu, Jiawei and Li, Gen and Zhou, Siyu and He, Qian and Wu, Xinglong},
  journal={arXiv preprint arXiv:2502.11079},
  year={2025}
}
```

## 📧 Contact
If you have any comments or questions regarding this open-source project, please open a new issue or contact [Tianxiang Ma](https://tianxiangma.github.io/).




python generate.py --task s2v-1.3B --size 832*480 --ckpt_dir ./Wan2.1-T2V-1.3B --phantom_ckpt ./Phantom-Wan-Models/Phantom-Wan-1.3B.pth  --ref_image "D:\hunyuan potraiuts\Phantom\test1.png" --prompt "暖阳漫过草地，扎着双马尾、头戴绿色蝴蝶结、身穿浅绿色连衣裙的小女孩蹲在盛开的雏菊旁。她身旁一只棕白相间的狗狗吐着舌头，毛茸茸尾巴欢快摇晃。小女孩笑着举起黄红配色、带有蓝色按钮的玩具相机，将和狗狗的欢乐瞬间定格。" --base_seed 42
