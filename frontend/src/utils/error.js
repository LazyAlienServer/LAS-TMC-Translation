import logger from "./logger";

function extractErrorMessage(err) {
    // axios backend response
    if (err?.response?.data?.detail) {
        return err.response.data.detail;
    }

    // axios response
    if (err?.response?.data) {
        return JSON.stringify(err.response.data);
    }

    // JS errors
    if (err?.message) {
        return err.message;
    }

    // last resort
    return String(err);
}

function setupGlobalErrorHandler(app) {
    app.config.errorHandler = function (error, instance, info) {
        const error_msg = extractErrorMessage(error);
        logger.error( 'Vue level error', {
            error: error_msg,
            info: info,
            component: instance?.$options?.name || 'anonymous',
        });

        // 你可以弹出一个 Toast（如果你用的是 vue-toastification 之类的）
        // showErrorToast('页面出错，请稍后重试');


        // 如果需要，统一做处理：比如跳转到错误页
    };

    // global JS errors
    window.onerror = function (message, source, lineno, colno, error) {
        logger.error('Window error', {
            message: message,
            error: extractErrorMessage(error),
            source: source,  // "error at file" url
            lineno: lineno,  // Line No.
            colno: colno,  // Column No.
        });
    };

    // unhandled Promise exceptions
    window.onunhandledrejection = function (event) {
        logger.error('Unhandled Promise rejection', {
            error: extractErrorMessage(event.reason),  // event.reason = error message
        });
    };
}


export {
    extractErrorMessage,
    setupGlobalErrorHandler,
}
