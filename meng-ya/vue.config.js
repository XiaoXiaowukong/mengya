// const BundleAnalyzerPlugin = require('webpack-bundle-analyzer').BundleAnalyzerPlugin
const SpeedMeasurePlugin = require('speed-measure-webpack-plugin')

const smp = new SpeedMeasurePlugin()
// const WebpackCdnPlugin = require('webpack-cdn-plugin');

module.exports = {
    configureWebpack: smp.wrap({
        plugins:[
            // process.env.NODE_ENV==='production'?new BundleAnalyzerPlugin():function(){},
            // new WebpackCdnPlugin({
            //     modules: [
            //       {
            //         name: 'vue',
            //         var: 'Vue',
            //         path: 'dist/vue.runtime.min.js'
            //       },
            //       {
            //         name: 'vue-router',
            //         var: 'VueRouter',
            //         path: 'dist/vue-router.min.js'
            //       },
            //       {
            //         name: 'vuex',
            //         var: 'Vuex',
            //         path: 'dist/vuex.min.js'
            //       },
            //       {
            //         name: 'leaflet',
            //         var: 'L',
            //         path: 'dist/leaflet.js'
            //       }
            //     ],
            //     publicPath: '/node_modules'
            //   })
        ]
    }),
    chainWebpack:config=>{
        config
          .plugin('html')
          .tap(args=>{
              args[0].title = '睿图东北模式后处理'
              return args;
          })
    },
    devServer: {
        host: '0.0.0.0',
        proxy: {
            "/api": {
                // target: "http://192.168.9.68:6852",
                target: "http://192.168.9.50:6868",
                changeOrigin: true,
                autoRewrite: true,
                cookieDomainRewrite: true,
                pathRewrite: {
                    '^/api': '/'
                }

            },
            "/static": {
                // target: "http://192.168.9.68:6868",
                target: "http://192.168.9.50:6868",
                changeOrigin: true,
                autoRewrite: true,
                cookieDomainRewrite: true,
            }

        }
    }
}
