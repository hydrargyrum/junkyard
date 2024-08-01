
#include <qt_windows.h>
#include <ActiveQt>
#include <QAxFactory>
#include "shelloverlay.h"

QT_USE_NAMESPACE


QAXFACTORY_DEFAULT(ShellOverlayBinder,
                   "{60c580d2-41f2-43ed-b5d1-b435d74d1999}", /* Class ID (CLSID) */
                   "{21a9e71b-9ae4-4887-8ada-720442394493}", /* Interface ID (IID) */
                   "{8c996c29-eafa-46ac-a6f9-901951e765b5}", /* event interface ID */
                   "{a6b1968a-4bbc-4420-9a55-5ce3579f795a}", /* Type Library ID (TLB) */
                   "{4f7d37e8-b9cb-4e66-a725-f043753b755c}" /* Application ID (AppID) */
                   )
