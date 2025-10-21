# drug_data.py
import pandas as pd

def get_drug_data():
    """
    Returns a DataFrame with the top 20 pediatric drugs, their adult doses,
    and modern mg/kg dosing guidelines.
    NOTE: Dosing information is for illustrative purposes ONLY and may not be
    clinically accurate. Always consult a professional medical source.
    """
    data = {
        'Drug': [
            'Amoxicillin', 'Ibuprofen', 'Paracetamol (Acetaminophen)', 'Azithromycin',
            'Cefdinir', 'Albuterol', 'Prednisolone', 'Cetirizine',
            'Montelukast', 'Ranitidine', 'Lorazepam', 'Ondansetron',
            'Diphenhydramine', 'Cephalexin', 'Clindamycin', 'Bactrim (SMX/TMP)',
            'Oseltamivir (Tamiflu)', 'Mupirocin', 'Nystatin', 'Methylphenidate'
        ],
        'Adult Dose (mg)': [
            500, 400, 650, 500, 300, 2.5, 20, 10, 10, 150, 2, 8, 50, 500, 300, 800, 75, 0, 500000, 20
        ],
        'Dose (mg/kg)': [
            30, 10, 15, 10, 14, 0.15, 1, 0.25, 0.15, 2, 0.05, 0.15, 1.25, 25, 10, 4, 3, 0, 100000, 0.5
        ],
        'Notes': [
            'Dosed per dose, 2-3 times/day', 'Per dose, every 6-8 hours', 'Per dose, every 4-6 hours', 'Once daily',
            'Dosed twice daily', 'Per dose (nebulizer)', 'Per day, often divided', 'Once daily',
            'Once daily', 'Twice daily', 'Per dose, as needed', 'Per dose', 'Per dose, every 6 hours',
            'Per dose, 2-4 times/day', 'Per dose, 3-4 times/day', 'Of SMX component, twice daily',
            'Twice daily', 'Topical, no systemic dose', 'Per dose, 4 times/day (units)', 'Per day, divided doses'
        ]
    }
    df = pd.DataFrame(data)
    return df

#The British National Formulary for Children (BNFc): A gold-standard pediatric drug formulary.

#The Harriet Lane Handbook: A renowned pediatric manual published by Johns Hopkins Hospital.

#Lexicomp Pediatric & Neonatal Dosage Handbook: A comprehensive professional drug database.

#Official Clinical Practice Guidelines: Published by organizations like the American Academy of Pediatrics (AAP).
