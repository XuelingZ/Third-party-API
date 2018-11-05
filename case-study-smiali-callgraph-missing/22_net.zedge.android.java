package com.google.firebase.auth;
public class FirebaseAuth implements zzeku {
    public interface C1457a {
        void onAuthStateChanged(@NonNull FirebaseAuth firebaseAuth);             //interface  onAuthStateChanged
    }
    
=================================================================================    
    
package p000;    
public final class dag implements Runnable {
    /* renamed from: a */
    private /* synthetic */ FirebaseAuth f20474a;

    public dag(FirebaseAuth firebaseAuth) {
        this.f20474a = firebaseAuth;
    }

    public final void run() {
        for (C1457a onAuthStateChanged : this.f20474a.f12021e) {
            onAuthStateChanged.onAuthStateChanged(this.f20474a);      //caller
        }
    }
}
    
================================================================================================
package net.zedge.android.log;    
public final class MarketplaceLogger$initLogger$1 implements C1457a {
    final /* synthetic */ Context $context;
    final /* synthetic */ FirebaseAuth $firebaseAuth;

    MarketplaceLogger$initLogger$1(Context context, FirebaseAuth firebaseAuth) {
        this.$context = context;
        this.$firebaseAuth = firebaseAuth;
    }

    public final void onAuthStateChanged(FirebaseAuth firebaseAuth) {
        eig.m21366b(firebaseAuth, "auth");
        daa c = firebaseAuth.mo17420c();
        if (c != null) {
            FirebaseAnalytics.getInstance(this.$context).setUserId(c.mo19447c());      //involk
            this.$firebaseAuth.mo17418b((C1457a) this);
        }
    }
}


===============================================================================================================    
    
    
package net.zedge.android.api.marketplace;
public final class MarketplaceServiceRetrofitWrapper implements C1457a, MarketplaceService {
 public final void onAuthStateChanged(FirebaseAuth firebaseAuth) {
        eig.m21366b(firebaseAuth, "auth");
        daa c = firebaseAuth.mo17420c();
        CharSequence c2 = c != null ? c.mo19447c() : null;
        Object obj = (c2 == null || c2.length() == 0) ? 1 : null;
        if (obj == null) {
            Object c3 = firebaseAuth.mo17420c();
            if (c3 == null) {
                eig.m21362a();
            }
            eig.m21363a(c3, "auth.currentUser!!");
            c3 = c3.mo19447c();
            eig.m21363a(c3, "auth.currentUser!!.uid");
            this.uid = c3;
            if (this.balance == -1) {
                getUserDataInternal(null);
            }
        }
    }
 }
