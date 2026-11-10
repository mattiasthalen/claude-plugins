# Assumptions

| Id | Assumption | Area | Stops holding when |
|----|------------|------|--------------------|
| A1 | `load_orders` reads the whole book into memory, and the book stays small enough for that. | orders / data file | The book passes 100,000 orders. |
| A2 | A GitHub Actions `schedule` trigger runs its cron expression in the repository owner's time zone, set to Europe/Stockholm in the account, so `0 2 * * *` fires at 02:00 Stockholm time. | ci / nightly count | The nightly count posts at another hour than 02:00 Stockholm time. |
