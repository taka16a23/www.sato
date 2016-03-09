CKEDITOR.plugins.add( 'timestamp',
{
	init: function( editor )
	{
		editor.addCommand( 'insertTimestamp',
				{
					exec : function( editor )
					{    
						var timestamp = new Date();
						editor.insertHtml( timestamp.getFullYear() + '年' + timestamp.getMonth() + '月' + timestamp.getDate() + '日' + timestamp.getHours() + '時' + timestamp.getMinutes() + '分');
					}
				});
		
		editor.ui.addButton( 'Timestamp',
				{
					label: '現在の時間を挿入',
					command: 'insertTimestamp',
					icon: this.path + 'images/timestamp.png'
				} );
	}
} );
