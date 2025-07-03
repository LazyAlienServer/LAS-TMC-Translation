const { defineConfig } = require('@vue/cli-service')
const path = require('path')
module.exports = defineConfig({
  transpileDependencies: true,

  configureWebpack: {
    resolve: {
      alias: {
        '@': path.resolve(__dirname, 'src')
      }
    }
  },

  devServer: {
    proxy: {
      '/api/v1': {
        target: 'http://web:8000', // Docker 容器内访问 Django 的服务名
        changeOrigin: true
      }
    }
  }
})
