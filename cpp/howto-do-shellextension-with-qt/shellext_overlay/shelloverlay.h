#ifndef SHELLOVERLAY_H
#define SHELLOVERLAY_H

#include "shellext_overlay_global.h"

#include <qt_windows.h>
#include <shlobj.h>

#include <QObject>
#include <QAxBindable>
#include <QAxAggregated>
#include <QUuid>

class ShellOverlayBinder : public QObject, public QAxBindable {
    Q_OBJECT

public:
    ShellOverlayBinder(QObject *parent = 0);

    QAxAggregated *createAggregate();

};

class SHELLEXT_OVERLAYSHARED_EXPORT ShellOverlay : public QObject, public QAxAggregated, public IShellIconOverlayIdentifier {
    Q_OBJECT

public:
    ShellOverlay(QObject *parent = 0);

    long queryInterface(const QUuid &iid, void**iface);
    // IUnknown
    QAXAGG_IUNKNOWN;

    // IShellIconOverlayIdentifier
    /*! Query information about the overlay icon
      \param pwszIconFile output parameter where to put the array of overlay icon (wchar_t **)
      \param cchMax size of the pwszIconFile buffer, in characters (not bytes)
      \param pIndex output parameter, index of the icon in the pwszIconFile file (e.g. if the file contains multiple icons), starting at 0
      \param pdwFlags output parameter, options for the overlay icon
      \return S_OK in case of success
      */
    STDMETHOD(GetOverlayInfo)(LPWSTR pwszIconFile, int cchMax, int *pIndex, DWORD* pdwFlags);

    STDMETHOD(GetPriority)(int* pPriority);

    /*! Query if the overlay is present for a particular file
      \param pwszPath path of the file to query (wchar_t*)
      \param dwAttrib attributes of the file
      \return S_OK if the icon has to be overlayed, S_FALSE else
      */
    STDMETHOD(IsMemberOf)(LPCWSTR pwszPath,DWORD dwAttrib);

};

#endif // SHELLOVERLAY_H
