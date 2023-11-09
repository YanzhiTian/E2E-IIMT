# pip install subword-nmt

subword-nmt learn-bpe -s 30000 < ./outputs/tok.de > ./outputs/bpecode.de
subword-nmt learn-bpe -s 30000 < ./outputs/tok.en > ./outputs/bpecode.en

subword-nmt apply-bpe -c ./outputs/bpecode.de < ./outputs/tok.de > ./outputs/seg.de
subword-nmt apply-bpe -c ./outputs/bpecode.en < ./outputs/tok.en > ./outputs/seg.en
