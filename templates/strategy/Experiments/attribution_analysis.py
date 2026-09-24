"""
Attribution analysis -- step 6 of 8, the fourth shared module.  Shapes what the KaxaNuk Attribution
Analysis library needs, and says what is missing before it tries.

In plain words: which part of the return did you actually earn?

Runs inside an experiment notebook, section 5, after the backtest.

What is expected here:

- Say what is present.  The library needs four inputs: an index's daily holdings and its daily
  returns, one or more factor-return files, and the book from step 5.  The first three are the
  desk's, read in place by `Data/hand_supplied.py` from the folder `KN_ANALYTICS_PATH` names, or
  from the drop zones under `Data/Curator/`.  Check for them first and report the gap in a
  sentence, so a clone with no licence and no index files pays nothing to find out.
- Take the book as a daily series, from `Backtest/`, never from `Portfolio/portfolio_weights.csv`.
  The library rejects a weight file that is not daily once it spans a year, and the rebalance-date
  file the engine read is exactly what it refuses.  The book it attributes is the one the engine
  held each trading day, drift and the cash proxy included; the benchmark's holdings follow the
  same rule.
- Widen the book to the benchmark before handing it over: every benchmark constituent the book
  does not hold, added at zero weight, each with its own price series.  The library prices only
  the securities named in the book, and the first cut computes the benchmark's return from those
  prices alone -- the index's own return series is never one of its inputs.  A book that names only
  what it holds is compared against the fraction of the index it happens to own, and the
  difference is reported as alpha, most of it filed under interaction, where nobody looks.  Drop
  the engine's benchmark column on the way, which it returns at zero, and keep the cash position.
- Shape the hand-supplied files into what the library's loader accepts, which is decided by **one
  cell**: the first header.  `Ticker` means securities down and dates across; `date_column` means
  dates down and securities across.  Anything else -- `date`, `m_date`, the name a provider happened
  to use -- raises before a number is read.  The same rule governs the book, the benchmark's
  holdings and the benchmark's return series, and none of them may carry nulls.  That is why the
  shaping lives here and not in a notebook.
- Say what the factor directory has to look like, because every entry in it is read as a factor
  file: one CSV per factor, a date column first -- its header may be empty -- and one column per
  security after it.  Four names are reserved by the library and dropped from the percentage
  decomposition: `f_market`, `f_total_factor_returns`, `f_total_excess_returns` and
  `f_idyo_returns`.  The desk ships them as `Market`, `Total_Factor_Returns`,
  `Total_Excess_Returns` and `Idyo_Returns`; `Data/hand_supplied.py` gives them the library's names,
  because a reserved file attributed as an ordinary factor is a quiet way to double-count the
  market.
- Name the two output files and the date convention once, so switching to a different index is an
  edit here and no notebook names a file.
- Capture the library's figures.  It shows them and returns nothing, so this module has to catch
  them on the way past and write them to `Attribution/`, then leave the plotting state as it found
  it.

Expect two methodologies and a third pass, all reported.  Brinson-Fachler splits active return
into allocation, selection and interaction -- the lever that moved.  The factor model splits
excess return into compensated factor tilts and idiosyncratic alpha -- what was paid for, on
purpose or by accident.  Then Brinson-Fachler again on the residual, which says whether the
Sharpe survives once the factor turns.  Expect the answer to be partial -- an absolute rule is
close to invisible to a factor model built on relative factors -- and treat that as a finding.
The follow-ups are counterfactual books the engine can already price.  `AGENTS.md` has the
reasoning.

It produces `Attribution/` -- the figures and the two decompositions -- for `FINDINGS_N.md`, and
the answer to graduation criterion 2.

It prevents selling factor beta as if it were alpha, and a run that stops at its first file because
a header carries the name a provider gave it rather than the one the loader expects.
"""
