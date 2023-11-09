bpe_time=30001

data_dir=

fairseq-preprocess --source-lang de --target-lang en \
    --trainpref ${data_dir}/bpe/${bpe_time}_bpe_train  \
    --validpref ${data_dir}/bpe/${bpe_time}_bpe_valid \
    --destdir ${data_dir}/data-bin-${bpe_time} \
    --workers 16
