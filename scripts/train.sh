data_dir=
model_dir=
bpe_time=

CUDA_VISIBLE_DEVICES=0,1,2,3 fairseq-train ${data_dir}/data-bin-${bpe_time} \
    -s de -t en \
    --save-dir ${model_dir}/bpe${bpe_time} \
    --max-update 500000 \
    --keep-best-checkpoints 5 \
    --save-interval-updates 5000 \
    --keep-interval-updates 5 \
    --no-epoch-checkpoints \
    --arch transformer_vaswani_wmt_en_de_big \
    --max-source-positions 2048 \
    --max-target-positions 2048 \
    --optimizer adam  \
    --adam-betas '(0.9, 0.98)'  \
    --lr-scheduler inverse_sqrt  \
    --warmup-init-lr 1e-07  \
    --warmup-updates 4000  \
    --lr 0.00005  \
    --stop-min-lr 1e-09  \
    --clip-norm 0  \
    --dropout 0.3  \
    --weight-decay 0.0001 \
    --criterion label_smoothed_cross_entropy  \
    --label-smoothing 0.1  \
    --max-tokens 2048  --update-freq 2 --batch-size-valid 20 \
    --skip-invalid-size-inputs-valid-test \
    --no-progress-bar \
    --fp16 --fp16-scale-tolerance 0.25 \
    --eval-bleu \
    --eval-bleu-args '{"beam": 1, "max_len_a": 1, "max_len_b": 50}' \
    --best-checkpoint-metric bleu --maximize-best-checkpoint-metric \
    --log-interval=100 2>&1 | tee bpe${bpe_time}.log
