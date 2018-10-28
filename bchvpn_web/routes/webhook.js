var express = require('express');
var router = express.Router();

/* GET webhook */
router.get('/', function(req, res, next) {
  res.send('GET respond with a resource');
});

/* POST webhook */
router.post('/', function(req, res, next) {
  res.send('POST respond with a resource: ' + req.body);
  console.log('POST respond with a resource: ' + req.body);
});

module.exports = router;
