package com.imangi.firebase;

public class UnityFirebaseBridge {
    
    public static boolean init(String inUserId) {                                //no caller
        boolean success = true;
        Context context = UnityPlayer.currentActivity.getApplicationContext();
        FirebaseApp firebaseApp = FirebaseApp.getInstance();
        FirebaseAnalytics analytics = FirebaseAnalytics.getInstance(context);
        if (firebaseApp == null) {
            Log.e(TAG, "FIREBASE init failed.  no app!");
            success = false;
        }
        if (analytics == null) {
            Log.e(TAG, "FIREBASE init failed.  no analytics!");
            return false;
        }
        LogMessage("Setting userId to " + inUserId);
        analytics.setUserId(inUserId);                                       //invoke
        return success;
    }
    
    
    public static void SetUserId(String inUserId) {                            // no caller
        LogMessage("FIREBASE - user id:" + inUserId);
        Context context = UnityPlayer.currentActivity.getApplicationContext();
        if (FirebaseAnalytics.getInstance(context) != null) {
            FirebaseAnalytics.getInstance(context).setUserId(inUserId);        //invoke
        } else {
            LogMessage("FIREBASE - NO ANALYTICS");
        }
    }
