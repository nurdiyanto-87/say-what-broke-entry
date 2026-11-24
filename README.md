# Say What Actually Broke

[![Say What Actually Broke](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5.svg)](https://make.fun/competitions/u-po-pu-say-what-actually-broke-a2c153b5)
[![Rank](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/nurdiyanto-87/say-what-broke-entry/rank.svg)](https://make.fun/competitions/u-po-pu-say-what-actually-broke-a2c153b5)
[![Reward](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/nurdiyanto-87/say-what-broke-entry/reward.svg)](https://make.fun/competitions/u-po-pu-say-what-actually-broke-a2c153b5)

An entry for the [Say What Actually Broke](https://make.fun/competitions/u-po-pu-say-what-actually-broke-a2c153b5) bounty on [make.fun](https://make.fun): one line of software error copy, at most 200 characters, that tells the user the brutal truth about what went wrong — and makes them laugh on the way.

## The entry

> Your backup finished without errors. It backed up an empty folder — faithfully, on schedule, for two years.

## How it works

`main.py` (pure Python standard library, no third-party imports) writes that single line to `/output/entry.txt` and validates it first: 1–200 characters, a single line, non-blank.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
