package com.fingersoft.game.firebase;
class C16891 implements ServiceConnection {
    protected void onCreate(Bundle bundle) {
        super.onCreate(bundle);
        int i = VERSION.SDK_INT;
        Log.m3487d(TAG, "onCreate");
        mActivityInstance = this;
        mFirebase = new Firebase(this);
        startAnalytics(null);                                // caller , null
      
      
    public static synchronized void startAnalytics(String str) {
        synchronized (MainActivity.class) {
            String str2 = TAG;
            StringBuilder stringBuilder = new StringBuilder();
            stringBuilder.append("Start analytics with uid: ");
            stringBuilder.append(str);
            Log.m3487d(str2, stringBuilder.toString());
            try {
                mAnalyticsUid = str;
                Log.m3487d(TAG, "Starting firebase analytics");
                mFirebase.initializeAnalyticsWithUserId(str, new C23939());
                mFirebase.getAnalyticsInstance().setUserID(str);                       // invoke
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
        return;
    }
      
