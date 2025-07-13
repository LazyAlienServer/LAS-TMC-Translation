import { sendLogToServer } from '@/api';
import { useUserStore } from "@/stores";


const LOG_LEVELS = ['debug', 'info', 'warn', 'error'];

function formatMessage(level, message, extra) {
    const timestamp = new Date().toISOString();
    return {
        level,
        message,
        extra,
        timestamp,
        page: window.location.pathname,
    };
}

function log(level, message, extra = {}) {
    if (!LOG_LEVELS.includes(level)) {
        throw new Error('Unknown log level: ' + level);
    }

    const userStore = useUserStore();
    const logEntry = formatMessage(level, message, {
        ...extra,
        userId: userStore?.userInfo?.id || null,
    });

    const levelColors = {
        debug: 'gray',
        info: 'blue',
        warn: 'yellow',
        error: 'red',
    };

    const css = `color: ${levelColors[level]}; font-weight: bold;`;

    console[level](
        `%c[${level.toUpperCase()}] ${logEntry.timestamp} (${logEntry.page})`,
        css,
        logEntry.message,
        logEntry.extra,
    )

    if (level === 'info' || level === 'warn' || level === 'error') {
        sendLogToServer(logEntry).catch((error) => {
            console.warn('Failed to send log to server', error);
        });
    }
}

export default {
    debug(message, extra) {
        log('debug', message, extra);
    },
    info(message, extra) {
        log('info', message, extra);
    },
    warn(message, extra) {
        log('warn', message, extra);
    },
    error(message, extra) {
        log('error', message, extra);
    },
};
