### An example of the end-to-end IIMT model mentioned in our paper, using 5 sentence pairs (text.de, text.en) to build image pairs.

----------------------------------------------------

#### 1. Build image

> Corresponding to the Section 3 in our paper.

```bash
bash build_img.sh
```

The output images are in folder `./de-en`.

#### 2. Convert image to pixel sequence (ITS)

> Corresponding to the Section 4.2 in our paper.

```bash
bash ITS.sh
```

The output pixel sequences are in `./outputs/tok.de` and `./outputs/tok.en`.

#### 3. Apply pixel sequence segmentation

> Corresponding to the Section 4.4 in our paper.

```bash
bash segment.sh
```

The lists of segmentation order (learned by BPE) are in `./outputs/bpecode.de` and `./outputs/bpecode.en`.

The output token sequences are in `./outputs/seg.de` and `./outputs/seg.en`.

#### 4. Train an NMT model

Train an NMT model with fairseq (https://github.com/pytorch/fairseq), including preprocess and train. You can refer to `../scripts/preprocess.sh` and `../scripts/train.sh`.

#### 5. Generate token sequence with NMT model

Generate token sequence with a well-trained NMT model. You can refer to `../scripts/generate.sh`.

#### 6. Convert pixel sequence to image (STI)

> Corresponding to the Section 4.3in our paper.

```bash
bash STI.sh
```

Assume the output of Step 5 is `./outputs/output_token_sequence.en`, applying STI to the token sequence.

The output images are in folder `./result`.



### An example of the evaluation of the IIMT model

--------------------------------------------------------------------------

#### 1. Recognize texts in the output images with an OCR model

```bash
bash ocr.sh
```

The OCR results are in `./outputs/result_ocr.en`.

#### 2. Compute BLEU score

```bash
cat ./outputs/result_ocr.en | sacrebleu text.en
```

#### 3. Compute COMET

```bash
comet-score -s text.de -t ./outputs/result_ocr.en -r text.en
```



**Note:  If you want to replicate our work, please use the filtered WMT14de-en corpus to construct the data.**
