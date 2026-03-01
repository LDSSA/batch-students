# LDSA Hackathon #5 — Roll the Dice: Board Game Recommendations

## Schedule

| Hour  | Activity |
|-------|----------|
| 08:15 | Arrival & setup |
| 08:30 | Hackathon prompt & team assignment |
| 09:00 | **Start hacking!** |
| 12:30 | Lunch (keep hacking if you like) |
| 14:00 | Goal — first submission |
| 15:00 | Goal — improved submission |
| 16:00 | Start working on presentation |
| 17:00 | **Stop hacking!** |
| 17:30 | Team presentations |
| 18:20 | Instructor's presentation |
| 18:30 | Winners announced |
| 18:45 | Closing remarks |

## Overview

Welcome to **Hackathon #5 — Roll the Dice**! 🎲

You've just been hired by **MeepleMatch**, a fast-growing board game discovery platform. MeepleMatch helps tabletop enthusiasts find their next favorite game, whether it's a 20-minute card game or an all-day strategy epic. The platform has thousands of games and tens of thousands of users, but the current recommendation page is just a static "Top Games" list. The CEO wants personalized recommendations, and she wants them yesterday.

Your mission: build a **board game recommendation system** that generates personalized suggestions for each user. You have user ratings and rich game metadata: categories, mechanics, player counts, complexity scores, and descriptions. Use everything at your disposal to help MeepleMatch users discover games they'll love.

## Data

You are provided with the following files:

### `train_interactions.csv` (4.2M rows)

User-game ratings from the BGG community.

| Column    | Type   | Description                                     |
|-----------|--------|-------------------------------------------------|
| `user`    | string | Username                                        |
| `game_id` | int   | Game ID (joins to metadata)                     |
| `rating`  | float  | Rating on a 1–10 scale                          |

- **49,821** unique users
- **20,422** unique games
- Sparsity: **99.6%** — most users have rated only a tiny fraction of all games

### `game_metadata.csv` (20,393 rows)

Rich metadata for each game.

| Column          | Type   | Description                                           |
|-----------------|--------|-------------------------------------------------------|
| `game_id`       | int    | Game ID (join key)                                    |
| `name`          | string | Game name                                             |
| `description`   | string | Text description (up to 1,000 chars)                  |
| `yearpublished` | int    | Year of publication                                   |
| `minplayers`    | int    | Minimum player count                                  |
| `maxplayers`    | int    | Maximum player count                                  |
| `playingtime`   | int    | Average play time in minutes                          |
| `minage`        | int    | Minimum recommended age                               |
| `categories`    | string | Pipe-separated categories (e.g. `Economic\|Negotiation`) |
| `mechanics`     | string | Pipe-separated mechanics (e.g. `Dice Rolling\|Hand Management`) |
| `complexity`    | float  | Complexity weight (1 = light, 5 = heavy)              |

### `test_users.json`

A JSON list of **1,500 user IDs** you must generate recommendations for.

### `sample_submission.json`

An example showing the expected submission format.

## Task

For each user in `test_users.json`, generate a ranked list of **10 board game IDs** that the user has **NOT** rated in the training data. Rank them from most to least relevant — the order matters!

## Evaluation

```
FinalRank = 0.5 × ModelPerformance_rank + 0.5 × Presentation_rank
```

Model performance is measured by **mAP@10** (Mean Average Precision at 10), computed against held-out interactions that users rated highly. Higher is better.

You can evaluate locally using `evaluate.py` on your own validation split before submitting to the leaderboard.

## Submission Format

Submit a JSON file named `submission.json`:

```json
{
  "some_user": ["1234", "5678", "91011", "1213", "1415",
                "1617", "1819", "2021", "2223", "2425"],
  "another_user": ["9876", "5432", ...]
}
```

- Every user in `test_users.json` **must** appear as a key
- Exactly **10 game IDs** per user (as strings)
- No games the user already rated in `train_interactions.csv`
- Max **5 submissions** to the leaderboard — choose wisely

## Rules

- Teams assigned randomly — work with who you've got
- Instructors answer technical questions, not solution questions
- No submissions after 17:00
- **4-minute** presentation hard limit — we will cut you off

## Presentation (4 minutes max)

Your presentation should be clear, structured, and informative:

1. Problem description and formulation
2. Data science workflow
3. Data exploration findings
4. Modeling approach and iterations
5. Results and interpretation
6. Recommendations / future work
7. A board-game-themed pun 🎲 (VERY IMPORTANT)


## Tips for Success

1. **Start with a non-personalized baseline immediately** — recommending the 10 most popular games to every user gets you on the leaderboard fast and sets a floor to beat.

2. **Build your interaction matrix as a sparse matrix** — with 50k users and 20k games, a dense matrix is ~8GB. Use `scipy.sparse.csr_matrix` instead.

3. **Try collaborative filtering next** — user-based or item-based kNN with cosine similarity are solid next steps. LightFM with WARP loss tends to outperform both.

4. **Use game metadata for content-based filtering** — TF-IDF on categories, mechanics, and descriptions lets you recommend games even for users with little rating history.

5. **Evaluate locally before submitting** — hold out some ratings as your own validation set and compute mAP@10. Don't burn your 5 submissions on guesses.

6. **Handle cold-start users explicitly** — some test users have very few ratings. If your model can't produce recommendations for them, fall back to popular games. Don't let them crash your pipeline.

7. **Optimize memory early** — downcast dtypes (`df['game_id'] = df['game_id'].astype('int32')`), and filter low-activity users/games before building matrices.

8. **Sanity-check your recommendations** — print the top-10 recs for a user who loves heavy strategy games. Are you recommending Catan clones or party games? Does it make sense?