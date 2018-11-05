package com.tabtale.publishingsdk.adsproviders.ironsourceadsproviders;
public class IronSourceAdsProviders implements InterstitialsAdsProviders {
    private IronSourceAdsProviders(Activity activity, String adKey, LocationInternalDelegate delegate, JSONObject attributes) {     
        try {
            IronSource.setISDemandOnlyInterstitialListener(new C40982());
            IronSource.setInterstitialListener(new C40993());
            IronSource.setUserId(this.mUserId);                                            // invoke, constructor
            if (this.mInstanceId != null) {
                IronSource.initISDemandOnly(this.mActivity, adKey, AD_UNIT.INTERSTITIAL);
                return;
            }
            IronSource.init(this.mActivity, adKey);
        } catch (Exception e2) {
            this.mEnabled = Boolean.valueOf(true);
            Log.v(TAG, "Exception " + e2.toString());
        }
    }
    
==============================================================================================================
package com.tabtale.publishingsdk.monetization.interstitials;

   protected void addProvider(List<InterstitialsAdsService> adsServices, String provider, String adKey, JSONObject attributes) {
         
            }  else if (provider.equalsIgnoreCase("applovin")) {
                service = new NativeInterstitialsAdsService(this.mAppInfo, this.mConnectivity, this.mConfigurationFetcher, adKey, "com.tabtale.publishingsdk.adsproviders.applovin.AppLovinInterstitialsAdsProviders", provider, this, attributes);
                if (service.mInterstitialsAdsProviders != null) {
                    adsServices.add(service);
                }
            } else if (provider.equalsIgnoreCase("mopub")) {      
                service = new NativeInterstitialsAdsService(this.mAppInfo, this.mConnectivity, this.mConfigurationFetcher, adKey, "com.tabtale.publishingsdk.adsproviders.mopub.MoPubInterstitialsAdsProviders", provider, this, attributes);
                if (service.mInterstitialsAdsProviders != null) {
                    adsServices.add(service);
                }
            } else if (provider.equalsIgnoreCase("ironsource")) {               // new ironsourceadsproviders
                service = new NativeInterstitialsAdsService(this.mAppInfo, this.mConnectivity, this.mConfigurationFetcher, adKey, "com.tabtale.publishingsdk.adsproviders.ironsourceadsproviders.IronSourceAdsProviders", provider, this, attributes);
                if (service.mInterstitialsAdsProviders != null) {
                    adsServices.add(service);
                }
            }
        }
    }
    
    
    
    public void onConfigurationFetched(boolean succeed) {        // caller
                        addProvider(adsServices, provider.getString("provider"), adKey, provider.optJSONObject("attributes"));
                        
