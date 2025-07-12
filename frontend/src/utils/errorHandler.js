function setupGlobalErrorHandler(app) {
    app.config.errorHandler = function (err, vm, info) {
        console.error('[Vue Error]:', err);
        console.warn('[Component]:', vm);
        console.warn('[Info]:', info);

        // 你可以弹出一个 Toast（如果你用的是 vue-toastification 之类的）
        // showErrorToast('页面出错，请稍后重试');

        // 你也可以做错误上报，例如：
        // sendToSentry(err, info);

        // 如果需要，统一做处理：比如跳转到错误页
        // router.push('/error')
    };
}

export {
    setupGlobalErrorHandler,
}
