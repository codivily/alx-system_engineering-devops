# install flask using pip3
class flask {
  package { 'flask':
    ensure   => '2.1.0',
    provider => 'pip3',
  }
}
include flask
