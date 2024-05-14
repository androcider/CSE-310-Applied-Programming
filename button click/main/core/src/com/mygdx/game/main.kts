import com.badlogic.gdx.ApplicationAdapter
import com.badlogic.gdx.Gdx
import com.badlogic.gdx.graphics.GL20
import com.badlogic.gdx.graphics.Texture
import com.badlogic.gdx.graphics.g2d.BitmapFont
import com.badlogic.gdx.graphics.g2d.SpriteBatch
import com.badlogic.gdx.scenes.scene2d.Stage
import com.badlogic.gdx.scenes.scene2d.ui.Skin
import com.badlogic.gdx.scenes.scene2d.ui.TextButton
import com.badlogic.gdx.scenes.scene2d.utils.ClickListener

class MyGame : ApplicationAdapter() {
    private lateinit var batch: SpriteBatch
    private lateinit var font: BitmapFont
    private lateinit var stage: Stage
    private lateinit var skin: Skin
    private lateinit var button: TextButton
    private var score: Int = 0

    override fun create() {
        batch = SpriteBatch()
        font = BitmapFont()
        stage = Stage()
        Gdx.input.inputProcessor = stage

        skin = Skin()
        val buttonStyle = TextButton.TextButtonStyle()
        buttonStyle.font = font
        skin.add("default", buttonStyle)

        button = TextButton("Tap the Button", skin)
        button.setPosition(Gdx.graphics.width / 2f - button.width / 2, Gdx.graphics.height / 2f - button.height / 2)
        button.addListener(object : ClickListener() {
            override fun clicked(event: com.badlogic.gdx.scenes.scene2d.InputEvent?, x: Float, y: Float) {
                score++
            }
        })

        stage.addActor(button)
    }

    override fun render() {
        Gdx.gl.glClearColor(1f, 1f, 1f, 1f)
        Gdx.gl.glClear(GL20.GL_COLOR_BUFFER_BIT)

        batch.begin()
        stage.act(Gdx.graphics.deltaTime)
        stage.draw()

        font.draw(batch, "Score: $score", 50f, Gdx.graphics.height - 50f)
        batch.end()
    }

    override fun dispose() {
        batch.dispose()
        font.dispose()
        stage.dispose()
        skin.dispose()
    }
}
