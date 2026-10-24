# My Blue iPhone Fund — iPhone 15 savings and price tracker

A personal savings dashboard for the exact phone you want:

**iPhone 15 · Blue · 128 GB · Excellent condition · Physical SIM + eSIM · unlocked**

- Starting savings: **£113.00**
- Starting reference price: **£338.00** (the price you last saw; not independently live-verified for Excellent condition)
- Estimated trade-in: **£320.00** (your estimate; final offer may change after inspection)
- Estimated extra fee: **£0.49** (Back Market says its Quality Assurance Fee starts at this amount)
- Estimated effective cost after trade-in at the starting reference: **£18.49**
- Savings target: the **full upfront price**, because Back Market may pay the trade-in after it receives and inspects your old phone. At £338 plus £0.49, with £113 already saved, the upfront amount left is **£225.49**.

The dashboard includes a savings progress ring, amount left to save, an estimated goal date, a price history chart, an activity diary, an editable weekly saving amount, a manual fallback price, an editable trade-in estimate, and export/import backups.

## Free hosting on GitHub Pages

This project is separate from your previous iPhone 16e site. Create a new repository called `iphone-15-blue-savings`. If you use the same GitHub account as your other site, the expected URL is `https://kvnn4329-ctrl.github.io/iphone-15-blue-savings/`.

1. Sign in to [GitHub](https://github.com/) and create a **new public repository** named `iphone-15-blue-savings`. Do not add a starter README.
2. Download and unzip this project ZIP on your computer.
3. On the new repository, choose **Add file → Upload files**. Upload the unzipped project contents, keeping the `.github`, `data`, `scripts`, and `tests` folders in the repository root.
4. Click **Commit changes** to the `main` branch.
5. Open **Settings → Pages** and set **Source = GitHub Actions**.
6. Open the **Actions** tab and select **Check exact iPhone 15 price and publish website**. Click **Run workflow** and choose `main`. If prompted, enable Actions for the repository.
7. When the deployment succeeds, open **Settings → Pages → Visit site**.

If the action fails with a push/permission error, open **Settings → Actions → General**, find **Workflow permissions**, and enable **Read and write permissions** if available, then rerun the workflow.

## About the price checker

- The website starts with **£338**, because that is the price you last saw. It is a **reference only**, not a claim that the current Excellent-condition listing costs £338. Search results for this exact listing have also shown Excellent at a different price, so check the selected condition and final checkout total before buying.
- The automated checker requests the exact Back Market page and only records a price if its selected product summary explicitly matches **iPhone 15 / Excellent / 128 GB / Physical SIM + eSIM / Blue**. It ignores generic condition-picker prices. If Back Market defaults to a different condition or changes its page, the checker will fail safely and keep the previous reference rather than guessing.
- GitHub Actions attempts checks approximately hourly. Schedules can be delayed, and Back Market can block automated requests or change its site. The dashboard labels reference, manual and verified prices differently.
- The **Refresh displayed price** button reloads the last published data file; it does not force a new merchant check. To request a new check, use **Actions → Check exact iPhone 15 price and publish website → Run workflow**.
- The workflow ignores commits that change only `data/price.json`, avoiding a loop where each price update triggers another workflow run.
- Price excludes any delivery or checkout costs not shown in the estimate. The quality assurance fee is an estimate and may vary.

## Trade-in and upfront cost

The tracker shows both the full upfront savings target and the effective cost after your estimated £320 trade-in. The savings progress uses the full upfront cost, since Back Market may only pay the trade-in after receiving and inspecting your old phone. Do not rely on the trade-in estimate until Back Market confirms it.

## Savings privacy

Your savings and transactions are stored in **this browser on this device**, not in the public GitHub repository. They do not sync automatically between devices. Clearing browser data may erase them, so use **Export backup** periodically. Use **Import backup** to restore a copy. The website does not need your Back Market login, does not make purchases, and does not store payment details.

## Local preview

Double-click `index.html` to try the dashboard. Savings controls should work in a browser that allows local storage for local files. Browsers often block local JSON fetches from `file://`, so the displayed reference is used in the preview; publish the site to GitHub Pages for the scheduled price checks.

## Test the price checker

Run:

```bash
python -m unittest discover -s tests -v
```

## Project files

- `index.html` — dashboard and settings dialogs
- `styles.css` — layout, styling and mobile support
- `app.js` — savings calculations, price display, chart, activity and backups
- `data/price.json` — published reference and price history
- `scripts/check_price.py` — checks only the exact selected product configuration
- `.github/workflows/price-and-pages.yml` — hourly checks and GitHub Pages deployment
- `tests/test_price_checker.py` — tests for variant matching and safeguards

*Independent personal tracker. Not affiliated with Apple or Back Market. Always confirm the selected condition and final price on Back Market before buying.*
