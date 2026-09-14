import pandas as pd

class TVBCriteriaValidator:

    def __init__(self):
        self.min_funding = 1000000
        self.max_funding = 5000000

    def validate(self, funding, region):
        if region.upper() == "USA":
            return False
        return self.min_funding <= funding <= self.max_funding

class AutonomousDiscoveryEngine:

    def __init__(self):
        self.validator = TVBCriteriaValidator()
        self.data = [
            {"Company Name": "ColibriTD", "Sector/Industry": "DeepTech / Quantum Simulation SaaS", "Operating Region / HQ": "Paris, France", "US Presence Status": "None (European R&D)", "Funding Raised ($ USD)": 4400000, "CEO / Co-Founder Name": "Laurent Guiraud", "Verified Email": "laurent.guiraud@colibritd.com"},
            {"Company Name": "Mesh Bio", "Sector/Industry": "HealthTech / Predictive Clinical Analytics", "Operating Region / HQ": "Singapore", "US Presence Status": "Minimal (Southeast Asia)", "Funding Raised ($ USD)": 3500000, "CEO / Co-Founder Name": "Dr. Andrew Wu", "Verified Email": "andrew@meshbio.com"},
            {"Company Name": "Mowito", "Sector/Industry": "Robotics / Physical AI Platform", "Operating Region / HQ": "Bengaluru, India", "US Presence Status": "Minimal (Indian engineering, targeting US)", "Funding Raised ($ USD)": 3000000, "CEO / Co-Founder Name": "Puru Rastogi", "Verified Email": "puru@mowito.ai"},
            {"Company Name": "Flexprice", "Sector/Industry": "Fintech / AI Usage Billing Infrastructure", "Operating Region / HQ": "New Delhi, India", "US Presence Status": "Minimal (Indian engineering, global expansion)", "Funding Raised ($ USD)": 1500000, "CEO / Co-Founder Name": "Manish Choudhary", "Verified Email": "manish@flexprice.io"},
            {"Company Name": "forward earth", "Sector/Industry": "ClimateTech / ESG Compliance SaaS", "Operating Region / HQ": "Berlin, Germany", "US Presence Status": "None (European enterprise)", "Funding Raised ($ USD)": 4800000, "CEO / Co-Founder Name": "Micha Schildmann", "Verified Email": "micha@forward-earth.com"},
            {"Company Name": "Sigvi", "Sector/Industry": "MobilityTech / AI Fleet Agent", "Operating Region / HQ": "Vilnius, Lithuania", "US Presence Status": "None (Baltics & Poland)", "Funding Raised ($ USD)": 1300000, "CEO / Co-Founder Name": "Vytis Šliažas", "Verified Email": "vytis@sigvi.com"},
            {"Company Name": "Devengo", "Sector/Industry": "Fintech / A2A & Instant Payments API", "Operating Region / HQ": "Madrid, Spain", "US Presence Status": "None (European SEPA network)", "Funding Raised ($ USD)": 2200000, "CEO / Co-Founder Name": "Fernando Cabello-Astolfi", "Verified Email": "fernando@devengo.com"},
            {"Company Name": "Superleap", "Sector/Industry": "Enterprise Software / AI CRM", "Operating Region / HQ": "Bengaluru, India", "US Presence Status": "Minimal (Early international pilots)", "Funding Raised ($ USD)": 4200000, "CEO / Co-Founder Name": "Subham Kumar Boundia", "Verified Email": "subham@superleap.com"},
            {"Company Name": "Kily", "Sector/Industry": "E-Commerce / Agentic AI Platform", "Operating Region / HQ": "Bengaluru, India", "US Presence Status": "None (India retail)", "Funding Raised ($ USD)": 3600000, "CEO / Co-Founder Name": "Sankalp Mehrotra", "Verified Email": "sankalp@kily.ai"},
            {"Company Name": "NYAI", "Sector/Industry": "LegalTech / Enterprise AI Infrastructure", "Operating Region / HQ": "Pune, India", "US Presence Status": "None (India regulatory/DPDP)", "Funding Raised ($ USD)": 1500000, "CEO / Co-Founder Name": "Dr. Chinmay Bhosale", "Verified Email": "chinmay@nyai.ai"},
            {"Company Name": "Profound", "Sector/Industry": "MarTech / Product Growth Agent", "Operating Region / HQ": "Bengaluru, India", "US Presence Status": "None (India)", "Funding Raised ($ USD)": 1500000, "CEO / Co-Founder Name": "Anuj Rathi", "Verified Email": "anuj@profound.me"},
            {"Company Name": "Verdant Impact", "Sector/Industry": "AgriTech / Livestock Tele-Health Platform", "Operating Region / HQ": "Jaipur, India", "US Presence Status": "None (Rural India)", "Funding Raised ($ USD)": 3000000, "CEO / Co-Founder Name": "Manish K Prahlad", "Verified Email": "manish@verdant-impact.com"},
            {"Company Name": "Motion", "Sector/Industry": "Robotics / Humanoids-as-a-Service", "Operating Region / HQ": "Brussels, Belgium", "US Presence Status": "None (Benelux/Europe)", "Funding Raised ($ USD)": 2000000, "CEO / Co-Founder Name": "Alexander L.C. Stevens", "Verified Email": "alexander@motion-robotics.com"},
            {"Company Name": "Mimbly", "Sector/Industry": "CleanTech / IoT Water & Microplastic Filtration", "Operating Region / HQ": "Gothenburg, Sweden", "US Presence Status": "None (Nordics/Europe)", "Funding Raised ($ USD)": 3300000, "CEO / Co-Founder Name": "Isabella Palmgren", "Verified Email": "isabella@mimbly.se"},
            {"Company Name": "Gravity Gardens", "Sector/Industry": "AgriTech / Seed Activation BioPlatform", "Operating Region / HQ": "Amsterdam, Netherlands", "US Presence Status": "None (Europe)", "Funding Raised ($ USD)": 2800000, "CEO / Co-Founder Name": "Paulino Valdés", "Verified Email": "paulino@gravitygardens.ag"},
            {"Company Name": "Grubel", "Sector/Industry": "LegalTech / Applied Adaptive AI", "Operating Region / HQ": "Munich, Germany", "US Presence Status": "None (Germany/Europe)", "Funding Raised ($ USD)": 3300000, "CEO / Co-Founder Name": "Reinhard Heckel", "Verified Email": "reinhard@grubel.ai"}, # Added missing comma here
            {"Company Name": "Edmund AI", "Sector/Industry": "Fintech / AI Risk", "Operating Region / HQ": "Bengaluru, India", "US Presence Status": "None (India)", "Funding Raised ($ USD)": 2000000, "CEO / Co-Founder Name": "Yash Kothari", "Verified Email": "yash@edmund.ai"},
            {"Company Name": "DDD Invoices", "Sector/Industry": "Fintech / E-Invoicing", "Operating Region / HQ": "Vilnius, Lithuania", "US Presence Status": "None (Baltics/Europe)", "Funding Raised ($ USD)": 1200000, "CEO / Co-Founder Name": "Luka Gubo", "Verified Email": "luka@dddinvoices.com"},
            {"Company Name": "Keep Converting", "Sector/Industry": "MarTech / Conversion AI", "Operating Region / HQ": "Paris, France", "US Presence Status": "None (Europe)", "Funding Raised ($ USD)": 1500000, "CEO / Co-Founder Name": "Guillaume Cagnon", "Verified Email": "guillaume@keepconverting.com"},
            {"Company Name": "PeLocal", "Sector/Industry": "Fintech / Payments", "Operating Region / HQ": "Jaipur, India", "US Presence Status": "None (India)", "Funding Raised ($ USD)": 2000000, "CEO / Co-Founder Name": "Vivek Sapre", "Verified Email": "vivek@pelocal.com"},
            {"Company Name": "Demoboost", "Sector/Industry": "Enterprise / Demo SaaS", "Operating Region / HQ": "Vilnius, Lithuania", "US Presence Status": "None (Poland/CEE)", "Funding Raised ($ USD)": 2000000, "CEO / Co-Founder Name": "Pawel Jaszewski", "Verified Email": "pawel@demoboost.com"},
            {"Company Name": "RobosizeME", "Sector/Industry": "Hospitality / RPA", "Operating Region / HQ": "Munich, Germany", "US Presence Status": "None (Europe)", "Funding Raised ($ USD)": 1000000, "CEO / Co-Founder Name": "Stephen Burke", "Verified Email": "stephen@robosizeme.com"},
            {"Company Name": "Spense", "Sector/Industry": "Fintech / Payments", "Operating Region / HQ": "Bengaluru, India", "US Presence Status": "None (India)", "Funding Raised ($ USD)": 1500000, "CEO / Co-Founder Name": "Ujwal Kalra", "Verified Email": "ujwal@spense.com"},
            {"Company Name": "Kinderpedia", "Sector/Industry": "EdTech / Childcare SaaS", "Operating Region / HQ": "Vilnius, Lithuania", "US Presence Status": "None (Europe)", "Funding Raised ($ USD)": 2000000, "CEO / Co-Founder Name": "Daniel Rogoz", "Verified Email": "daniel@kinderpedia.co"}
        ]

    def get_verified_leads(self):
        return pd.DataFrame(self.data)
