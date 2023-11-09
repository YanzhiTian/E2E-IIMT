bpe_time=
data_dir=
model_dir=
input_prefix=
batch=10
gpu=0

for split in "valid" "test"; do
    echo "fairseq interactive "${split}" ......"
    mkdir ./${split}/${bpe_time}
    CUDA_VISIBLE_DEVICES=${gpu} fairseq-interactive ${data_dir} \
        --input ${input_prefix}/${bpe_time}_bpe_${split}.de \
        --path ${model_dir} \
        --max-len-a 1 --max-len-b 200 \
        --buffer-size ${batch} \
        --max-source-positions 2048 \
        --max-target-positions 2048 \
	    --skip-invalid-size-inputs-valid-test \
        --batch-size ${batch} --beam 5 > ${input_prefix}/${bpe_time}_bpe_${split}.bestbeam5.txt
    grep ^H ${input_prefix}/${bpe_time}_bpe_${split}.bestbeam5.txt | cut -f3- > ${input_prefix}/output_token_sequence.en
done
