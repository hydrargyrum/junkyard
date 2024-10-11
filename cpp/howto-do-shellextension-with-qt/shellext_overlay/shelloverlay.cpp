#include "shelloverlay.h"

#include <QFileInfo>
#include <QAxFactory>

/* binder definitions */
ShellOverlayBinder::ShellOverlayBinder(QObject *parent) : QObject(parent) {}

QAxAggregated *ShellOverlayBinder::createAggregate() {
        return new ShellOverlay(this);
}

/* overlay definition */
ShellOverlay::ShellOverlay(QObject *parent) : QObject(parent) {}


STDMETHODIMP ShellOverlay::GetOverlayInfo(LPWSTR pwszIconFile, int cchMax, int *pIndex, DWORD *pdwFlags) {
        QString iconPath(QAxFactory::serverFilePath());
        if (iconPath.length() > cchMax)
                return S_FALSE;

        int len = iconPath.toWCharArray(pwszIconFile);
        pwszIconFile[len] = L'\0';

        *pIndex = 0;
        *pdwFlags = ISIOI_ICONFILE | ISIOI_ICONINDEX;

        return S_OK;
}

STDMETHODIMP ShellOverlay::GetPriority(int *pPriority) {
        *pPriority = 0;
        return S_OK;
}

STDMETHODIMP ShellOverlay::IsMemberOf(LPCWSTR pwszPath, DWORD dwAttrib) {
        QFileInfo finfo(QString::fromWCharArray(pwszPath));
        QString filename = finfo.fileName();
        if (filename.contains(QChar('q')) || filename.contains(QChar('t')))
                return S_OK;
        return S_FALSE;
}

long ShellOverlay::queryInterface(const QUuid &iid, void **iface) {
        *iface = 0;
        if (iid == IID_IShellIconOverlayIdentifier)
                *iface = (IShellIconOverlayIdentifier *)this;
        else
                return E_NOINTERFACE;

        AddRef();
        return S_OK;
}
