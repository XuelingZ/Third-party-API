package com.halfbrick.mortar;
public class Provider_AppsFlyerBackend {
    public static void Initialise(final String str, final String str2) {                  //no caller
            MortarGameActivity.sActivity.runOnUiThread(new Runnable() {
                public void run() {
                    try {
                        Log.d("AppsFlyer", "Setting appKey: " + str);
                        AppsFlyerLib.getInstance().setCustomerUserId(str2);                 //caller
                        AppsFlyerLib.getInstance().startTracking(MortarGameActivity.sActivity.getApplication(), str);
                        AppsFlyerLib.getInstance().registerConversionListener(MortarGameActivity.sActivity, new C18941());
                    } catch (Throwable th) {
                        Log.e("AppsFlyer", "Failed to initialise AppsFlyer SDK");
                        Log.d("AppsFlyer", "AppsFlyer appKey: " + str);
                    }
                }
            });
    }
}
                
                
        
             
