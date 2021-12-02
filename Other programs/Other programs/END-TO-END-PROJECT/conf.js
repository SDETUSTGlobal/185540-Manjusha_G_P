exports.config = {
    framework: 'jasmine', //Type of Framework used 
    directConnect:true, 
    specs: ['spec1.js', 'spec2.js', 'spec3.js', 'spec4.js', 'spec5.js'], //Name of the Specfile 
    onPrepare() { 
          require('ts-node').register({ 
          project: require('path').join(__dirname, './tsconfig.json') // Relative path of tsconfig.json file 
        });
    } 
}
//'spec1.js', 'spec2.js', 'spec3.js', 'spec4.js', 'spec5.js'