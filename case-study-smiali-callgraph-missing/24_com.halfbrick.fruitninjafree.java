package com.halfbrick.mortar;
public class Provider_AppsFlyerBackend {
    private static Activity s_activity;
    
    
    public static void onCreate() {
        String GetAppKey = GetAppKey();
        String GetDeviceID = GetDeviceID();                                                // parameter
        if (GetAppKey == null || GetAppKey.equals("")) {
            Log.e("halfbrick.Mortar.AppsFlyerBackend", "onCreate> AppKey not found.");
        } else if (GetDeviceID == null || GetDeviceID.equals("")) {
            Log.e("halfbrick.Mortar.AppsFlyerBackend", "onCreate> DeviceID not found.");
        } else {
            Log.d("halfbrick.Mortar.AppsFlyerBackend", "onCreate> Initializing...");
            StartTracking(GetAppKey, GetDeviceID);                           //   caller
        }
    }
    
    
    
    private static void StartTracking(String str, String str2) {
        try {
            Log.d("halfbrick.Mortar.AppsFlyerBackend", "StartTracking> DeviceID  : " + str2);
            Log.d("halfbrick.Mortar.AppsFlyerBackend", "StartTracking> appKey    : " + str);
            AppsFlyerLib.getInstance().setCustomerUserId(str2);                                   //  invoke
            AppsFlyerLib.getInstance().startTracking(s_activity.getApplication(), str);
        } catch (Throwable th) {
            Log.e("halfbrick.Mortar.AppsFlyerBackend", "StartTracking> Failed to initialise AppsFlyer SDK");
            Log.e("halfbrick.Mortar.AppsFlyerBackend", "StartTracking> AppsFlyer appKey: " + str);
            Log.e("halfbrick.Mortar.AppsFlyerBackend", "" + th.getClass() + " thrown: " + th);
        }
    }
    
     private static String GetDeviceID() {
        return NativeGameLib.GetDeviceID();
    }
    
    =======================================================================================================
package com.halfbrick.mortar;
public class NativeGameLib {
    private static native String native_GetDeviceID();      // parameter, native interfacce   
        
        
        
