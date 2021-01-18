let p = new Promise((reslove,reject) => {
    // setTimeout( () => {
    //   console.log('timeout')
      reslove()
    // }, 1000)
})
p.then(v => {
    console.log('start')
})