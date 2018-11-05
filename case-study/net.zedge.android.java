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
            FirebaseAnalytics.getInstance(this.$context).setUserId(c.mo19447c());
            this.$firebaseAuth.mo17418b((C1457a) this);
        }
    }
