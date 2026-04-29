module.exports = {
  css: { extract: false },
  chainWebpack: config => {
    config.module
      .rule('vue')
      .use('vue-loader')
      .tap(options => {
        options.shadowMode = true;
        return options;
      });
  }
};
