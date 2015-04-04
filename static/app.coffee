app = angular.module 'app', [
  'ui.router'
  'restangular'
  'satellizer'
]
.config (
    $stateProvider, $urlRouterProvider,
    $compileProvider,
    RestangularProvider,
    $authProvider) ->

  # Performance
  $compileProvider.debugInfoEnabled(false)

  # Load Materialize components
  $('.modal-trigger').leanModal()
  #$('a.brand-logo').tabs()
  $('ul.tabs').tabs()

  # REST APIs
  RestangularProvider.setBaseUrl '/api/v1'
  RestangularProvider.setRequestSuffix '/'
  $authProvider.loginUrl = '/api-token-auth/'

  # URLs
  $urlRouterProvider
    .otherwise 'summary'

  # States
  $stateProvider
    .state 'summary', {
      url: 'summary'
      templateUrl: 'static/partials/summary.html'
      resolve:
        groups: (Restangular) ->
          Restangular.all('groups').getList()
        techniques: (Restangular) ->
          Restangular.all('techniques').getList()

      controller: ($scope, groups, techniques) ->
        $scope.groups = groups
        _.forEach $scope.groups, (group) ->
          _.forEach group.patrols, (patrol) ->
            _.forEach patrol.tests, (test) ->
              test.technique_name = _.result(_.filter(techniques, { 'id': test.technique })[0], 'name')
    }

    .state 'ranking', {
      url: 'ranking'
      templateUrl: 'static/partials/ranking.html'
      resolve:
        patrols: (Restangular) ->
          Restangular.all('patrols').getList()

      controller: ($scope, patrols) ->
        $scope.patrols = patrols
    }

    .state 'techniques', {
      url: 'techniques'
      templateUrl: 'static/partials/techniques.html'
      resolve:
        techniques: (Restangular) ->
          Restangular.all('techniques').getList()

      controller: ($scope, techniques) ->
        $scope.techniques = techniques
    }

    .state 'tests', {
      url: 'tests'
      templateUrl: 'static/partials/tests.html'
      resolve:
        tests: (Restangular) ->
          Restangular.all('tests').getList()
        patrols: (Restangular) ->
          Restangular.all('patrols').getList()
        techniques: (Restangular) ->
          Restangular.all('techniques').getList()

      controller: ($state, $scope, techniques, tests, patrols) ->
        $scope.tests = tests

        _.forEach $scope.tests, (test) ->
          test.technique_name = _.result(_.find(techniques, { 'id': test.technique }), 'name')
          patrol = _.filter(patrols, { 'id': test.patrol })[0]
          test.patrol_name = patrol.name
          test.group_name = patrol.group

        # Reload the page every 5s
        _.delay ->
          $state.reload 'tests'
        , 5000
    }

    .state 'addtest', {
      url: 'addtest'
      templateUrl: 'static/partials/addtest.html'
      resolve:
        patrols: (Restangular) ->
          Restangular.all('patrols').getList()
        groups: (Restangular) ->
          Restangular.all('groups').getList()
        techniques: (Restangular) ->
          Restangular.all('techniques').getList()
      
      controller: ($state, $auth, $rootScope, $scope, Restangular, patrols, groups, techniques) ->
        $('.modal-trigger').leanModal()
        $scope.newTest = {}
        $scope.feedback = ''
        $scope.search = { group: undefined }

        $scope.techniques = techniques
        $scope.groups = groups
        $scope.patrols = patrols

        $scope.save = ->
          saveThisTest =
            technique_score: $scope.newTest.technique_score
            style_score: $scope.newTest.style_score
            technique: _.result(_.find($scope.techniques, { 'name': $scope.newTest.technique }), 'id')
            patrol: _.result(_.find($scope.patrols, { 'name': $scope.newTest.patrol, 'group': $scope.search.group }), 'id')
            user: $rootScope.username

          Restangular.service('tests').post saveThisTest
            .then () ->
              $scope.feedback =
                data: 'Test added successfully!'
              $state.reload 'addtest'
            , (feedback) ->
              $scope.feedback = feedback
          $('#confirm-add-test').closeModal()

    }
  return


.run ($rootScope, $auth, $state) ->

  $rootScope.login = ->
    $auth.login
      username: $rootScope.username
      password: $rootScope.password

    if $rootScope.isAuth()
      $state.go 'addtest'
    else
      $rootScope.msg = 'Error'

  $rootScope.logout = ->
    $auth.logout()
    #if not $auth.isAuthenticated()
    if not $rootScope.isAuth()
      $state.go 'summary'

  $rootScope.isAuth = ->
    #$auth.isAuthenticated()
    if $auth.getToken()
      true

  $rootScope.goHome = ->
    $('ul.tabs').tabs('select_tab', 'tab4')
    $state.go 'summary'

  $state.go 'summary'
