/**
 * Portrait Studio — Central Configuration Object
 * Single source of truth for branding, contact, and legal variables.
 * Replace the values below or use scripts/replace-variables.py prior to public launch.
 */
const SITE_CONFIG = {
  app: {
    name: "Portrait Studio",
    isProvisionalName: true,
    internalCodename: "RetroPortrait",
    tagline: "Back to 1985. Your next '80s photo.",
    shortDescription: "Transform a selected photo into an authentic 1980s-style portrait with private processing and verified credit unlocks.",
    appStoreUrl: "REPLACE_BEFORE_PUBLISHING_APP_STORE_URL"
  },
  operator: {
    legalName: "REPLACE_BEFORE_PUBLISHING_OPERATOR_LEGAL_NAME",
    jurisdiction: "REPLACE_BEFORE_PUBLISHING_JURISDICTION",
    supportEmail: "REPLACE_BEFORE_PUBLISHING_SUPPORT_EMAIL",
    privacyEmail: "REPLACE_BEFORE_PUBLISHING_PRIVACY_EMAIL",
    mailingAddress: "REPLACE_BEFORE_PUBLISHING_MAILING_ADDRESS"
  },
  dates: {
    effectiveDate: "October 1, 2026",
    lastUpdated: "October 1, 2026"
  },
  urls: {
    baseUrl: "https://portrait-studio.github.io",
    home: "/",
    privacy: "/privacy/",
    terms: "/terms/",
    support: "/support/",
    privacyChoices: "/privacy-choices/",
    appleEula: "https://www.apple.com/legal/internet-services/itunes/dev/stdeula/"
  },
  commercialModel: {
    introductoryPreviews: "2 watermarked previews per new account",
    monthlyStarterCredits: 10,
    monthlyPlusCredits: 25,
    topUpPacks: [10, 25],
    creditCostPerCleanPortrait: 1,
    pricingNotice: "Current localized pricing appears inside the iOS app and on the App Store product page."
  },
  retention: {
    unpaidGenerationHours: 12,
    unlockedGenerationHours: 48
  }
};

if (typeof module !== 'undefined' && module.exports) {
  module.exports = SITE_CONFIG;
}
