# Example: ai-interface-patterns

## Input

> Design the UX for an AI assistant in our analytics product that answers
> questions about the user's data in plain English ("why did signups drop last
> week?").

## Output

# Ask-Your-Data Assistant — Interface Design

## Feature frame
Input: a natural-language question. Output: an answer + the chart/query it's based on. Stakes: medium — people may make decisions on it, so being *verifiable* matters. It reads data; it doesn't take actions.

## Core interaction
Input box (with starter questions) → on submit, show a "working" trace ("interpreting question → querying → summarizing") → **stream** the answer text → render the **chart/table** it used, plus the actual query. Feels fast; user sees the reasoning, not a black box.

## Trust & verifiability
- Every answer shows **the query it ran and the chart/data** behind it — one click to inspect. This is the core trust move: the user can check the work.
- Output labeled "AI-generated — verify against the data."
- Numbers in the prose link to the chart cells they came from.

## Uncertainty & no-answer
- If the question is ambiguous ("recently"?), the assistant **asks a clarifying question** instead of guessing a timeframe.
- If the data can't answer it (not tracked), say so plainly: "We don't track X, so I can't answer that — here's what I do have." No fabricated number.
- Low confidence (sparse data) → shows a caveat banner, not a confident claim.

## Control
- **Stop** generation mid-stream. **Regenerate**. **Edit the question** and re-run. **"Show me the query"** to tweak it directly (power users). Thumbs + "this is wrong" that logs the case.

## Errors & latency
- Query timeout/error → "Couldn't run that — try narrowing the date range / Retry," never a raw error. Long queries stream a progress trace; skeleton for the chart. Fallback: a link to build the chart manually.

## First-run / empty state
- Empty box shows 4 starter questions grounded in *their* data ("Why did signups drop last week?", "Which channel converts best?") so users learn what they can ask.

## Patterns intentionally skipped
- Heavy tool-use transparency beyond the query trace — overkill for a read-only Q&A. No human-in-the-loop approval — it doesn't take actions (would add it if it did).
