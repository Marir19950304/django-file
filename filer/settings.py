import os
from django.conf import settings

FILER_IS_PUBLIC_DEFAULT = getattr(settings, 'FILER_IS_PUBLIC_DEFAULT', False)

FILER_STATICMEDIA_PREFIX = os.path.normpath( getattr(settings, 'FILER_STATICMEDIA_PREFIX', os.path.join(settings.MEDIA_URL,'filer/') ) ) + '/'

FILER_PUBLICMEDIA_PREFIX = os.path.normpath( getattr(settings, 'FILER_PUBLICMEDIA_PREFIX', 'filer_public') )
FILER_PRIVATEMEDIA_PREFIX = os.path.normpath( getattr(settings, 'FILER_PRIVATEMEDIA_PREFIX', 'filer_private') )

# please don't change these in settings for now. all media dirs must be beneath MEDIA_ROOT!
FILER_PUBLICMEDIA_URL = os.path.normpath( getattr(settings, 'FILER_PUBLICMEDIA_URL', os.path.join(settings.MEDIA_URL,FILER_PUBLICMEDIA_PREFIX) ) )
FILER_PUBLICMEDIA_ROOT = os.path.abspath( os.path.join(settings.MEDIA_ROOT, FILER_PUBLICMEDIA_PREFIX ) )

FILER_PRIVATEMEDIA_URL = os.path.normpath( getattr(settings, 'FILER_PRIVATEMEDIA_URL', os.path.join(settings.MEDIA_URL,FILER_PRIVATEMEDIA_PREFIX) ) )
FILER_PRIVATEMEDIA_ROOT = os.path.abspath( os.path.join(settings.MEDIA_ROOT, FILER_PRIVATEMEDIA_PREFIX ) )


FILER_ADMIN_ICON_SIZES = (
        '32','48','64',
)