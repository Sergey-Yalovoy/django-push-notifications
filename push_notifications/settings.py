from django.conf import settings


PUSH_NOTIFICATIONS_SETTINGS = getattr(settings, "PUSH_NOTIFICATIONS_SETTINGS", {})

PUSH_NOTIFICATIONS_SETTINGS.setdefault(
	"CONFIG", "push_notifications.conf.LegacyConfig"
)

# GCM
PUSH_NOTIFICATIONS_SETTINGS.setdefault(
	"GCM_POST_URL", "https://android.googleapis.com/gcm/send"
)
PUSH_NOTIFICATIONS_SETTINGS.setdefault("GCM_MAX_RECIPIENTS", 1000)
PUSH_NOTIFICATIONS_SETTINGS.setdefault("GCM_ERROR_TIMEOUT", None)

# FCM
PUSH_NOTIFICATIONS_SETTINGS.setdefault(
	"FCM_POST_URL", "https://fcm.googleapis.com/fcm/send"
)
PUSH_NOTIFICATIONS_SETTINGS.setdefault("FCM_MAX_RECIPIENTS", 1000)
PUSH_NOTIFICATIONS_SETTINGS.setdefault("FCM_ERROR_TIMEOUT", None)

# APNS
if settings.DEBUG:
	PUSH_NOTIFICATIONS_SETTINGS.setdefault("APNS_USE_SANDBOX", True)
else:
	PUSH_NOTIFICATIONS_SETTINGS.setdefault("APNS_USE_SANDBOX", False)
PUSH_NOTIFICATIONS_SETTINGS.setdefault("APNS_USE_ALTERNATIVE_PORT", False)
PUSH_NOTIFICATIONS_SETTINGS.setdefault("APNS_TOPIC", None)

# WNS
PUSH_NOTIFICATIONS_SETTINGS.setdefault("WNS_PACKAGE_SECURITY_ID", None)
PUSH_NOTIFICATIONS_SETTINGS.setdefault("WNS_SECRET_KEY", None)
PUSH_NOTIFICATIONS_SETTINGS.setdefault(
	"WNS_ACCESS_URL", "https://login.live.com/accesstoken.srf"
)

# WP (WebPush)
PUSH_NOTIFICATIONS_SETTINGS.setdefault("WP_POST_URL", {
	"CHROME": PUSH_NOTIFICATIONS_SETTINGS["FCM_POST_URL"],
	"OPERA": PUSH_NOTIFICATIONS_SETTINGS["FCM_POST_URL"],
	"FIREFOXV2": "https://updates.push.services.mozilla.com/wpush/v2",
	"FIREFOXV1": "https://updates.push.services.mozilla.com/wpush/v1",
	"EDGE": "https://wns2-par02p.notify.windows.com/w",
	"SAFARI": "https://web.push.apple.com",
})
PUSH_NOTIFICATIONS_SETTINGS.setdefault("WP_PRIVATE_KEY", None)
PUSH_NOTIFICATIONS_SETTINGS.setdefault("WP_CLAIMS", None)
PUSH_NOTIFICATIONS_SETTINGS.setdefault("WP_ERROR_TIMEOUT", None)

# User model
PUSH_NOTIFICATIONS_SETTINGS.setdefault("USER_MODEL", settings.AUTH_USER_MODEL)

# Unique registration ID for all devices
PUSH_NOTIFICATIONS_SETTINGS.setdefault("UNIQUE_REG_ID", False)

# API endpoint settings
PUSH_NOTIFICATIONS_SETTINGS.setdefault("UPDATE_ON_DUPLICATE_REG_ID", False)
