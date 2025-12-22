import api from './axiosInstance'

function getSourceArticles() {
    return api.get('/article/source_articles/', { withCredentials: true });
}

function getMySourceArticles() {
    return api.get('/article/source_articles/mine/', { withCredentials: true });
}

function getPendingArticles() {
    return api.get('/article/article_snapshots/pending/', { withCredentials: true });
}

function getTheSourceArticle(id) {
    return api.get(`/article/source_articles/${id}/`, { withCredentials: true });
}

function createSourceArticle() {
    return api.post(`/article/source_articles/`)
}

function updateSourceArticle(id, title, content) {
    return api.patch(
        `/article/source_articles/${id}/`,
        {
            title: title,
            content: content,
        },
        { withCredentials: true },
    )
}

function submitArticle(id) {
    return api.post(
        `/article/article_actions/${id}/submit/`,
        {article_id: id},
        { withCredentials: true }
    );
}

function withdrawArticle(id) {
    return api.post(
        `/article/article_actions/${id}/withdraw/`,
        {},
        { withCredentials: true }
    );
}

function approveArticle(id) {
    return api.post(
        `/article/article_actions/${id}/approve/`,
        {},
        { withCredentials: true }
    );
}

function rejectArticle(id) {
    return api.post(
        `/article/article_actions/${id}/reject/`,
        {},
        { withCredentials: true }
    );
}

function unpublishArticle(id) {
    return api.post(
        `/article/article_actions/${id}/unpublish/`,
        {},
        { withCredentials: true }
    );
}

function deleteArticle(id) {
    return api.post(
        `/article/article_actions/${id}/delete/`,
        {},
        { withCredentials: true }
    );
}

export {
    getSourceArticles,
    getMySourceArticles,
    getPendingArticles,
    getTheSourceArticle,
    createSourceArticle,
    updateSourceArticle,
    submitArticle,
    withdrawArticle,
    approveArticle,
    rejectArticle,
    unpublishArticle,
    deleteArticle,
}
