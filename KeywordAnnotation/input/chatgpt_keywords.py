gpt = {'Immigration': ["asylum seekers", "naturalization", "family reunification", "border control",
                       "border security", "detention centers", "entry restrictions", "immigration policy",
                       "border enforcement", "guest workers", "undocumented workers", "immigration reform",
                       "work permits", "temporary protected status", "immigration laws", "citizenship rights",
                       "human trafficking", "immigration debate", "integration", "asylum", "birthright citizenship",
                       "migration patterns", "cross-border movement", "immigrant communities", "border issues",
                       "border patrol", "immigration quota", "border crossing", "asylum process", "deportation",
                       "inclusion", "exclusion", "border policies", "border crisis", "resettlement", "border barriers",
                       "migration flows", "border control measures", "border management", "immigrant integration",
                       "immigration enforcement", "border restrictions", "migration policy", "border tensions",
                       "border conflicts", "border disputes", "human rights", "multiculturalism",
                       "nation of immigrants"],
       'Islamophobia': [
           "xenophobia", "discrimination", "hate crimes", "stereotyping", "racial profiling",
           "stigmatization", "prejudice", "bigotry", "persecution", "intolerance", "scapegoating",
           "religious bias", "hate speech", "anti-Muslim rhetoric", "cultural ignorance",
           "racial tensions", "minority marginalization", "hijabi", "anti-Islamic sentiment",
           "Islamophobic violence", "xenophobic attacks", "religious intolerance", "hijabophobia",
           "Islamophobic propaganda", "anti-Muslim propaganda", "discriminatory policies",
           "counterterrorism measures", "Islamist extremism", "anti-Muslim sentiment",
           "Muslim-majority countries", "Muslim ban", "Islamophobic incidents", "religious profiling",
           "anti-Muslim discrimination", "radicalization", "Islamist terrorism", "hate crimes against Muslims",
           "discrimination against Muslims", "religious freedom", "Islamophobia awareness",
           "anti-Muslim prejudice", "Muslim community", "anti-Islamophobia activism", "media representation",
           "Muslim identity", "mosque attacks", "hijab ban", "Islamophobia reporting", "Islamophobia legislation",
           "Allah", "Prophet Muhammad", "Qur'an", "Sunnah", "Hadith", "Hajj", "Umrah", "Salat",
           "Zakat", "Sawm", "Ramadan", "Eid", "Mecca", "Medina", "Islamic", "Muslim", "Ummah",
           "Sharia", "Halal", "Haram", "Iftar", "Suhoor", "Mosque", "Imam", "Mufti", "Muezzin",
           "Islamic law", "Islamic culture", "Islamic faith", "Islamic teachings", "Islamic beliefs",
           "Islamic traditions", "Islamic practices", "Muslim community", "Muslim identity",
           "Muslim-majority countries", "Islamic world", "Islamic scholarship", "Islamic art",
           "Islamic architecture", "Islamic civilization", "Islamic history", "Islamic education",
           "Islamic philosophy", "Islamic spirituality", "Islamic festivals", "Islamic holidays",
           "Islamic values", "Islamic ethics", "Islamic morality", "Islamic jurisprudence",
           "Islamic reform", "Islamic extremism", "Islamic feminism", "Islamic finance",
           "Islamic spirituality", "Islamic literature", "Islamic science", "Islamic medicine",
           "Islamic contributions", "Islamic revival", "Muslim scholars", "Muslim philosophers",
           "Muslim scientists", "Muslim leaders", "Muslim thinkers", "Muslim activists",
           "Muslim artists", "Muslim writers", "Muslim women", "Muslim men", "Muslim youth",
           "Muslim immigrants", "Muslim refugees", "Muslim diaspora"
       ],
       'Anti-semitism': [
           "Holocaust denial", "discrimination", "prejudice", "stereotyping", "scapegoating",
           "hate crimes", "hate speech", "anti-Semitic rhetoric", "racial bias", "religious bias",
           "anti-Semitic propaganda", "xenophobia", "religious intolerance", "racial tensions",
           "minority persecution", "Jewish community", "Jewish identity", "Jewish heritage",
           "Jewish culture", "Jewish religion", "Jewish traditions", "Jewish practices",
           "Jewish history", "Jewish values", "Jewish ethics", "Jewish literature", "Jewish art",
           "Jewish scholarship", "Jewish leaders", "Jewish thinkers", "Jewish activists",
           "Jewish artists", "Jewish writers", "Jewish organizations", "Jewish immigrants",
           "Jewish refugees", "anti-Semitism awareness", "Jewish diaspora", "anti-Semitic incidents",
           "anti-Semitic prejudice", "media representation", "anti-Semitism reporting",
           "anti-Semitism legislation", "Jewish resistance", "genocide", "concentration camps",
           "extermination camps", "Nazi", "Swastika", "Auschwitz", "Kristallnacht", "Nuremberg Laws",
           "Jewish persecution", "Jewish victims", "Righteous Among the Nations"
       ],
       'Transphobia': [
           "gender identity", "gender expression", "trans rights", "trans activism",
           "gender dysphoria", "gender-affirming", "gender nonconforming", "trans visibility",
           "trans community", "trans individuals", "trans inclusivity", "gender stereotypes",
           "cisnormativity", "misgendering", "deadnaming", "gender-affirming care",
           "gender-affirming surgery", "social transition", "medical transition",
           "transition process", "transphobia awareness", "transphobic incidents",
           "transphobic prejudice", "LGBTQ+ rights", "gender diversity", "genderqueer identity",
           "gender spectrum", "gender acceptance", "gender variance", "transgender equality",
           "gender equality", "transgender representation", "transgender issues",
           "transgender discrimination", "transgender healthcare", "gender-affirming healthcare",
           "transgender support", "transgender awareness", "transgender advocacy",
           "transgender acceptance", "transgender visibility", "transgender activism",
           "transgender empowerment", "gender-affirming policies", "gender-affirming legislation"
       ]}

connotation = {"Immigration": {'positive': [
    "citizenship", "migration", "immigration", "foreign workers", "refugees",
    "immigrant", "migrants", "visa holders", "dream act", "resettlement",
    "immigrant integration", "human rights", "multiculturalism", "nation of immigrants"],
    'negative': [
        "undocumented", "illegal aliens", "refugee", "sanctuary cities", "green card",
        "deport", "anti-immigration", "open border", "illegal immigrants", "xenophobic",
        "illegals", "visa waiver", "border walls", "border surge", "asylum seekers",
        "border control", "border security", "detention centers", "entry restrictions",
        "border enforcement", "undocumented workers", "immigration reform", "temporary protected status",
        "immigration laws", "human trafficking", "border crisis", "border barriers",
        "immigration enforcement", "border restrictions", "border tensions", "border conflicts",
        "border disputes"]},
    'Islamophobia': {'negative': [
        "xenophobia", "hate crimes", "stereotyping", "stigmatization", "prejudice",
        "hate speech", "anti-Muslim rhetoric", "cultural ignorance", "Islamophobic violence",
        "xenophobic attacks", "hijabophobia", "Islamophobic propaganda", "anti-Muslim propaganda",
        "Islamist extremism", "anti-Muslim sentiment", "Muslim-majority countries",
        "Muslim ban", "Islamophobic incidents", "religious profiling", "anti-Muslim discrimination",
        "hate crimes against Muslims", "discrimination against Muslims", "Muslimophobia",
        "Islamophobia awareness", "anti-Muslim prejudice", "media representation", "mosque attacks",
        "hijab ban", "Islamophobia reporting", "Islamophobia legislation"
    ],
        'positive': [
            "hijabi", "Islamophobic awareness", "interfaith dialogue", "religious tolerance",
            "inclusivity", "multiculturalism", "Muslim community", "Muslim identity",
            "Islamic culture", "Islamic art", "Islamic architecture", "Islamic civilization",
            "Islamic history", "Islamic education", "Islamic philosophy", "Islamic spirituality",
            "Islamic feminism", "Islamic finance", "Islamic literature", "Islamic science",
            "Islamic medicine", "Islamic contributions", "Islamic revival", "Muslim scholars",
            "Muslim philosophers", "Muslim scientists", "Muslim leaders", "Muslim thinkers",
            "Muslim activists", "Muslim artists", "Muslim writers", "Muslim women", "Muslim men",
            "Muslim youth", "Muslim immigrants", "Muslim refugees", "Muslim diaspora"
        ]

    }
    ,
    'Anti-semitism': {'positive': [
        "Jewish community", "Jewish identity", "Jewish heritage", "Jewish culture",
        "Jewish religion", "Jewish traditions", "Jewish practices", "Jewish history",
        "Jewish values", "Jewish ethics", "Jewish literature", "Jewish art", "Jewish scholarship",
        "Jewish leaders", "Jewish thinkers", "Jewish activists", "Jewish artists", "Jewish writers",
        "Jewish organizations", "Jewish immigrants", "Jewish refugees", "anti-Semitism awareness",
        "Jewish diaspora", "Jewish resistance", "Righteous Among the Nations"
    ]
        ,
        'negative': [
            "Holocaust denial", "discrimination", "prejudice", "stereotyping", "scapegoating",
            "hate crimes", "hate speech", "anti-Semitic rhetoric", "anti-Semitic propaganda",
            "xenophobia", "religious intolerance", "racial tensions", "minority persecution",
            "anti-Semitic incidents", "anti-Semitic prejudice", "media representation",
            "anti-Semitism reporting", "anti-Semitism legislation", "genocide",
            "concentration camps", "extermination camps", "Nazi", "Swastika", "Auschwitz",
            "Kristallnacht", "Nuremberg Laws", "Jewish persecution", "Jewish victims"
        ]
    },
    'Transphobia': {'positive': [
        "transgender", "gender transition", "non-binary", "gender-affirming",
        "gender nonconforming", "trans visibility", "trans community",
        "trans inclusivity", "genderqueer identity", "gender spectrum",
        "transgender equality", "gender equality", "transgender representation",
        "transgender issues", "transgender healthcare", "gender-affirming healthcare",
        "transgender support", "transgender awareness", "transgender advocacy",
        "transgender acceptance", "transgender visibility", "transgender activism",
        "transgender empowerment", "gender-affirming policies", "gender-affirming legislation"
    ]
        ,
        'negative': [
            "biological woman", "pronoun", "transphobic", "anti-trans", "biological males",
            "transphobia", "bathroom bill", "transsexuals"
        ]
    }
}

pos = {
    'Immigration': ['citizenship', 'migration', 'undocumented', 'refugees', 'immigrant', 'migrant', 'sanctuary cities', 'green card', 'guest workers', 'undocumented workers', 'citizenship rights', 'migration patterns', 'immigrant communities', 'migration flows', 'immigrant integration', 'birthright citizenship', 'nation of immigrants'],
    'Islamophobia': ['hijabi', 'islamophobia awareness', 'interfaith dialogue', 'religious tolerance', 'inclusivity', 'multiculturalism', 'Muslim community', 'Muslim identity', 'Muslim-majority countries', 'Islamic scholarship', 'Islamic art', 'Islamic architecture', 'Islamic civilization', 'Islamic history', 'Islamic education', 'Islamic philosophy', 'Islamic spirituality', 'Islamic feminism', 'Islamic finance', 'Islamic literature', 'Islamic science', 'Islamic medicine', 'Islamic contributions', 'Islamic revival', 'Muslim scholars', 'Muslim philosophers', 'Muslim scientists', 'Muslim leaders', 'Muslim thinkers', 'Muslim activists', 'Muslim artists', 'Muslim writers', 'Muslim women', 'Muslim men', 'Muslim youth', 'Muslim immigrants', 'Muslim refugees', 'Muslim diaspora'],
    'Anti-semitism': ['Jewish community', 'Jewish identity', 'Jewish heritage', 'Jewish culture', 'Jewish religion', 'Jewish traditions', 'Jewish practices', 'Jewish history', 'Jewish values', 'Jewish ethics', 'Jewish literature', 'Jewish art', 'Jewish scholarship', 'Jewish leaders', 'Jewish thinkers', 'Jewish activists', 'Jewish artists', 'Jewish writers', 'Jewish organizations', 'Jewish immigrants', 'Jewish refugees', 'anti-Semitism awareness', 'Jewish diaspora', 'Jewish resistance', 'Righteous Among the Nations'],
    'Transphobia': ['transgender', 'gender transition', 'non-binary', 'gender-affirming', 'gender nonconforming', 'trans visibility', 'trans community', 'trans inclusivity', 'genderqueer identity', 'gender spectrum', 'transgender equality', 'gender equality', 'transgender representation', 'transgender issues', 'transgender healthcare', 'gender-affirming healthcare', 'transgender support', 'transgender awareness', 'transgender advocacy', 'transgender acceptance', 'transgender visibility', 'transgender activism', 'transgender empowerment', 'gender-affirming policies', 'gender-affirming legislation']
}

# Negative connotation keywords for each topic
neg = {
    'Immigration': ['border wall', 'illegal aliens', 'foreign workers', 'illegal entry', 'refugee', 'deport', 'anti-immigration', 'open border', 'illegal immigrants', 'xenophobic', 'illegals', 'visa waiver', 'dream act', 'border walls', 'border surge', 'asylum seekers', 'deportation', 'border patrol', 'asylum process', 'border control', 'immigration policy', 'border enforcement', 'temporary protected status', 'immigration laws', 'immigration debate', 'border crisis', 'border barriers', 'migration policy', 'migration'],
    'Islamophobia': ['sharia', 'jihad', 'jihadist', 'jihadism', 'jihadists', 'islamists', 'burqa', 'koran', 'islamization', 'hijabs', 'muslims', 'hijab', 'jihadi', 'muslim', 'anti-muslim', 'islamic fundamentalists', 'islam', 'islamophobia', 'radical islam', 'islamophobic', 'islamic extremism', 'anti-islam', 'sunni', 'shia', 'sunnis'],
    'Anti-semitism': ['anti-semitism', 'anti-semitic', 'gas chamber', 'antisemitic', 'judaism', 'judeo', 'extermination camps'],
    'Transphobia': ['biological woman', 'pronoun', 'transphobic', 'anti-trans', 'biological males', 'transphobia', 'bathroom bill', 'transsexuals']
}
