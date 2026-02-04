import streamlit as st
import pandas as pd
import numpy as np
import joblib
import tldextract
import re

# Load saved model, scaler, and feature columns
model = joblib.load("siteshield_model.pkl")
scaler = joblib.load("siteshield_scaler.pkl")
feature_cols = joblib.load("siteshield_feature_cols.pkl")

# ------------------------------------
# 🔥 Feature Extraction from URL
# ------------------------------------
def extract_features(url):
    ext = tldextract.extract(url)

    hostname = ext.domain + "." + ext.suffix
    path = url.split(ext.suffix)[-1]

    features = {
        'NumDots': url.count('.'),
        'SubdomainLevel': len(ext.subdomain.split('.')) if ext.subdomain else 0,
        'PathLevel': path.count('/'),
        'UrlLength': len(url),
        'NumDash': url.count('-'),
        'NumDashInHostname': hostname.count('-'),
        'AtSymbol': url.count('@'),
        'TildeSymbol': url.count('~'),
        'NumUnderscore': url.count('_'),
        'NumPercent': url.count('%'),
        'NumQueryComponents': url.count('='),
        'NumAmpersand': url.count('&'),
        'NumHash': url.count('#'),
        'NumNumericChars': sum(ch.isdigit() for ch in url),
        'NoHttps': 0 if url.startswith("https") else 1,
        'RandomString': 1 if re.search(r'[A-Za-z0-9]{10,}', url) else 0,
        'IpAddress': 1 if re.match(r"\d+\.\d+\.\d+\.\d+", hostname) else 0,
        'DomainInSubdomains': 1 if ext.domain in ext.subdomain else 0,
        'DomainInPaths': 1 if ext.domain in path else 0,
        'HttpsInHostname': 1 if "https" in hostname else 0,
        'HostnameLength': len(hostname),
        'PathLength': len(path),
        'QueryLength': len(url.split('?')[-1]) if '?' in url else 0,
        'DoubleSlashInPath': 1 if '//' in path else 0,
        'NumSensitiveWords': sum(w in url.lower() for w in ['login', 'secure', 'update']),
        'EmbeddedBrandName': 1 if any(b in url.lower() for b in ['paypal', 'amazon', 'google']) else 0,
        'PctExtHyperlinks': 0,
        'PctExtResourceUrls': 0,
        'ExtFavicon': 0,
        'InsecureForms': 0,
        'RelativeFormAction': 0,
        'ExtFormAction': 0,
        'AbnormalFormAction': 0,
        'PctNullSelfRedirectHyperlinks': 0,
        'FrequentDomainNameMismatch': 0,
        'FakeLinkInStatusBar': 0,
        'RightClickDisabled': 0,
        'PopUpWindow': 0,
        'SubmitInfoToEmail': 0,
        'IframeOrFrame': 0,
        'MissingTitle': 0,
        'ImagesOnlyInForm': 0,
        'SubdomainLevelRT': 0,
        'UrlLengthRT': 0,
        'PctExtResourceUrlsRT': 0,
        'AbnormalExtFormActionR': 0,
        'ExtMetaScriptLinkRT': 0,
        'PctExtNullSelfRedirectHyperlinksRT': 0,
    }

    # Filter features to match model training features exactly
    df = pd.DataFrame([features])[feature_cols]
    scaled = scaler.transform(df)
    prediction = model.predict(scaled)[0]

    return prediction

# ------------------------------------
# 🌐 STREAMLIT UI
# ------------------------------------
st.title("🔐 SiteShield – Real-Time Phishing Detection System")
st.write("Enter any website URL below and check if it is **Phishing or Legitimate**.")

url_input = st.text_input("Enter Website URL", "")

if st.button("Check Website"):
    if url_input.strip() == "":
        st.error("Please enter a valid URL!")
    else:
        result = extract_features(url_input)

        if result == 1:
            st.error("⚠️ Warning: This website appears to be **PHISHING**!")
        else:
            st.success("✅ This website appears to be **LEGITIMATE**.")
