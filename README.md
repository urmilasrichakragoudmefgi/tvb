# Autonomous Discovery Engine 🚀

Hey there! Welcome to the Autonomous Discovery Engine repository. 

This is a lightweight Python utility built to track, validate, and manage early-stage global tech startups. If you're hunting for promising international leads that match specific funding and regional criteria (like staying clear of the US or keeping investments right in that sweet seed/Series A spot), this tool has your back.

## What's Inside?

- **`TVBCriteriaValidator`**: A quick rules engine that filters companies based on funding limits ($1M – $5M) and geographic presence (excluding the USA).
- **`AutonomousDiscoveryEngine`**: Houses a curated dataset of verified global startups across AI, Fintech, DeepTech, AgriTech, and more, complete with leadership contacts and verified emails.

## Quick Start

Make sure you have `pandas` installed, then drop the script into your project:

```bash
pip install pandas
```

```python
from engine import AutonomousDiscoveryEngine

# Initialize the engine
engine = AutonomousDiscoveryEngine()

# Get all verified leads as a clean pandas DataFrame
df_leads = engine.get_verified_leads()
print(df_leads.head())
```

## Dataset Snapshot

The engine comes pre-loaded with international startups headquartered across Europe, Southeast Asia, and India, tracking fields like:
- Company Name & Sector/Industry
- Operating Region / HQ
- Funding Raised ($ USD)
- CEO / Co-Founder & Verified Email

## Contributing

Got a new startup lead or want to tweak the validation criteria? PRs and issues are always welcome. Just open up a branch and submit your changes!
