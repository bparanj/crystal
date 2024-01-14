gem 'rspec'
gem 'rantly'
gem 'rspec-rails', '~> 5.0', '>= 5.0.1'


require 'rails_helper'
require 'rantly/rspec_extensions'

RSpec.describe 'Rack Application', type: :request do
  let(:rack_app) { Pbt::Application.new }

  it 'responds to call and returns an array of [status, headers, body]' do
    property_of {
      Rantly { dict(10) { [string, string] } }
    }.check { |env|
      status, headers, body = rack_app.call(env)
      expect(status).to be_a(Integer)
      expect(headers).to be_a(Hash)
      expect(body).to be_a(Rack::BodyProxy)
    }
  end
end
