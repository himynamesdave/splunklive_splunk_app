//
//   Copyright 2015 by Johan Bjerke, <jbjerke@splunk.com>
//
//
//   Unless required by applicable law or agreed to in writing, software
//   distributed under the License is distributed on an "AS IS" BASIS,
//   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
//   See the License for the specific language governing permissions and
//   limitations under the License.
//

define(function(require, exports, module) {
    var _ = require('underscore');
    var mvc = require('splunkjs/mvc');

    var SimpleSplunkView = require('splunkjs/mvc/simplesplunkview');
    var ImageGrid = SimpleSplunkView.extend({
        className: "imagegrid",
        options: {
            managerid: null,
            data: "preview",
            urlField: null
        },

        createView: function() {
            this.$el.html('');
            return true;
        },

        updateView: function(viz, data) {
            $el = this.$el
            // console.log("The data object: ", data);
            // get settings from simple xml
            var collection = data;
            var url = this.settings.get('urlField') || [];

            var div = $('<div></div>');
            div.attr('class', "imagegrid");

            // create div.col tag for every url found in the search
            for (var i=0; i < collection.length; i++){
              var col = $('<div></div>');
              col.attr('class', "col-md-15");
			
              // TODO: collection[i][0] is totally ugly and buggy
              var img = $('<img src="'+collection[i][0]+'" />');
              //var img = $('<img src="/static/app/custom_simplexml_extensions/custom_pics/pic1.jpg" />');
              img.attr('width', '92%');
              img.appendTo(col);
              
              if (i % 5 == 0) {
              		var row = $('<div></div>');
              		row.attr('class', "row");
            	}
              
              col.appendTo(row);
              row.appendTo(div);
            }

            // append ul tag to DOM
            div.appendTo($el);

        }
    });
    return ImageGrid;
});
