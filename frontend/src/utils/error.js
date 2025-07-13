function extractErrorMessage(err) {
    if (err?.response?.data?.detail) {
        return err.response.data.detail;
    }

    if (err?.response?.data) {
        return JSON.stringify(err.response.data);
    }

    if (err?.message) {
        return err.message;
    }

    return String(err);
}

export {
    extractErrorMessage,
}
